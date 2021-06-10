#! /bin/bash

rm -rf {RPMS,SOURCES,SPECS,SRPMS}
mkdir {RPMS,SOURCES,SPECS,SRPMS}

for SPEC in $(ls SPECS/*); do
    mock -r fedora-rawhide-x86_64 --buildsrpm --spec ${SPEC} --sources SOURCES
    mv /var/lib/mock/fedora-rawhide-x86_64/result/*.src.rpm SRPMS
done

for LINE in $(grep -v '^#' goipaths.txt | tac); do
    IPATH=$(echo "${LINE}" | cut -d\, -f1)
    FORGE=$(echo "${LINE}" | cut -d\, -f2)
    SUBDIR=$(echo "${LINE}" | cut -d\, -f3)
    ALTIPATHS=$(echo "${LINE}" | cut -d\, -f4)
    VERSION=$(echo "${LINE}" | cut -d\, -f5)
    TAG=$(echo "${LINE}" | cut -d\, -f6)
    COMMIT=$(echo "${LINE}" | cut -d\, -f7)
    SRC=$(echo "${LINE}" | cut -d\, -f8)
    DST=$(echo "${LINE}" | cut -d\, -f9)
    pushd SPECS
    ARGUMENTS="--no-auto-changelog-entry --clean "
    if [ "${IPATH}" == "" ]; then
        echo "Missing ipath."
        exit 1
    fi
    if [ "${FORGE}" != "" ]; then
        ARGUMENTS+="--forge ${FORGE} "
    fi
    if [ "${SUBDIR}" != "" ]; then
        ARGUMENTS+="--subdir ${SUBDIR} "
    fi
    if [ "${ALTIPATHS}" != "" ]; then
        ALTIPATHS=$(echo "${ALTIPATHS}" | sed -e 's/_/\ /g')
        ARGUMENTS+="--altipaths ${ALTIPATHS} "
    fi
    if [ "${VERSION}" != "" ]; then
        ARGUMENTS+="--version ${VERSION} "
    fi
    if [ "${TAG}" != "" ]; then
        ARGUMENTS+="--tag ${TAG} "
    fi
    if [ "${COMMIT}" != "" ]; then
        ARGUMENTS+="--commit ${COMMIT} "
    fi
    CMD="go2rpm ${ARGUMENTS} ${IPATH}"
    echo "${CMD}"
    SLEEP=0
    SUMMARY=0
    SPEC=""
    while [ ${SLEEP} -lt 31 -a ${SUMMARY} -eq 0 ]; do
        echo -n "sleeping for ${SLEEP} seconds..."
        sleep ${SLEEP}
        echo "done."
        echo "trying ${CMD}"
        bash -c "${CMD}"
        SPEC=$(grep -H "^%global goipath         ${IPATH}$" *.spec | cut -d: -f1)
        grep '^Summary:        None$' ${SPEC}
        SUMMARY=$?
        let SLEEP=${SLEEP}+10
    done
    if [ "https://${IPATH}" != "${FORGE}" ]; then
        ESCFORGE=$(echo "${FORGE}" | sed -e 's/\//\\\//g')
        sed -i -e '/%global forgeurl /d' ${SPEC}
        sed -i -e "/^%global goipath .*/a %global forgeurl        ${ESCFORGE}" ${SPEC}
    fi
    ../go2rpm-sort ${SPEC}
    ../go2rpm-docs ${SPEC}
    ../go2rpm-build ${SPEC}
    popd
    pushd SOURCES
    ../go2rpm-dl ../SPECS/${SPEC}
    if [ "${SRC}" != "" -a "${DST}" != "" ]; then
        mv -v ${SRC} ${DST}
    fi
    popd
    mock -r fedora-rawhide-x86_64 --buildsrpm --spec SPECS/${SPEC} --sources SOURCES
    mv /var/lib/mock/fedora-rawhide-x86_64/result/*.src.rpm SRPMS
done

mock -r fedora-rawhide-x86_64 --chain --recurse $(for s in SRPMS/*.src.rpm; do r=$(rpm -qp --requires ${s} | grep '^golang(' | wc -l) && t=$(stat -c %W ${s}) && echo ${r},${t},${s}; done  | sort -n | cut -d, -f3) 2>&1 | tee build.log

