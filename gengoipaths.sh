#! /bin/bash

echo "#IPATH,FORGE,SUBDIR,ALTIPATHS,VERSION,TAG,COMMIT,SRCTGZ,DSTTGZ,TYPE" > goipaths.txt
echo "#IPATH,SUMMARY,DESCRIPTION" > goipaths-docs.txt

for MOD in $(cat packages.txt); do
    echo "========== BEGIN ${MOD} =========="

    GOIMPORT=$(curl -s "https://${MOD}?go-get=1" | grep '<meta ' | grep ' name="go-import"' | grep -P -o ' content=".*"' | cut -d\" -f2)
    if [ "${GOIMPORT}" == "" ]; then
        GOIMPORT=$(curl -s "http://${MOD}?go-get=1" | grep '<meta ' | grep ' name="go-import"' | grep -P -o ' content=".*"' | cut -d\" -f2)
        if [ "${GOIMPORT}" == "" ]; then
            GOIMPORT="${MOD} git https://${MOD}.git"
        fi
    fi

    ROOTPATH=$(echo ${GOIMPORT} | awk '{print $1}')
    VCS=$(echo ${GOIMPORT} | awk '{print $2}')
    REPOURL=$(echo ${GOIMPORT} | awk '{print $3}' | sed -e 's/\.git//g')

    ESCROOTPATH=$(echo "${ROOTPATH}" | sed -e 's/\//\\\//g' | sed -e 's/\./\\\./g')
    ROOTSUBDIR=$(echo "${MOD}" | sed -e "s/^${ESCROOTPATH}//g" | sed -e 's/^\///g')
    PKGGODEVURL="https://pkg.go.dev/${ROOTPATH}"

    if [ "${ROOTSUBDIR}" != "" ]; then
        PKGGODEVURL="${PKGGODEVURL}/${ROOTSUBDIR}"
        REPOURL="${REPOURL}/${ROOTSUBDIR}"
    fi

    PKGGODEVFILE=$(mktemp)
    CURLRET=1
    while [ ${CURLRET} -ne 0 ]; do
        curl -f -s "${PKGGODEVURL}" > ${PKGGODEVFILE}
        CURLRET=$?
        if [ ${CURLRET} -ne 0 ]; then
            PKGGODEVURL=$(dirname ${PKGGODEVURL})
            REPOURL=$(dirname ${REPOURL})
        fi
    done

    FORGE=$(grep -A 7 Repository ${PKGGODEVFILE} | grep -P -o '<a href=".*" ' | cut -d\" -f2 | grep -P -o "https:\/\/.*")
    DVERSION=$(grep -P 'data-version=".*"' ${PKGGODEVFILE} | head -1 | cut -d\" -f2 | sed -e 's/\+incompatible//g')
    DMODPATH=$(grep -P 'data-mpath=".*"' ${PKGGODEVFILE} | head -1 | cut -d\" -f2)
    DPKGPATH=$(grep -P 'data-ppath=".*"' ${PKGGODEVFILE} | head -1 | cut -d\" -f2)
    DTYPE=$(grep -P 'data-pagetype=".*"' ${PKGGODEVFILE} | head -1 | cut -d\" -f2)

    ESCDMODPATH=$(echo "${DMODPATH}" | sed -e 's/\//\\\//g' | sed -e 's/\./\\\./g')
    SUBDIR=$(echo ${DPKGPATH} | sed -e "s/^${ESCDMODPATH}//g" | sed -e 's/^\///g')
    FORGEALTIPATH=$(echo ${FORGE} | sed -e 's/^http:\/\///g' | sed -e 's/^https:\/\///g')
    REPOALTIPATH=$(echo ${REPOURL} | sed -e 's/^http:\/\///g' | sed -e 's/^https:\/\///g')
    if [ "${DVERSION}" == "" ]; then
        DVERSION="HEAD"
    fi
    grep -q "^${DMODPATH}$" packages.txt
    if [ $? -ne 0 ]; then
        echo "${DMODPATH}" >> packages.txt
    fi
    VERSION=$(basename ${DVERSION} | sed -e 's/^v//g')
    TAG=${DVERSION}
    IPATH=${DPKGPATH}
    ALTIPATHS=""
    TYPE=${DTYPE}

    if [ "${FORGEALTIPATH}" != "${IPATH}" ]; then
        ALTIPATHS+=" ${FORGEALTIPATH}"
    fi
    if [ "${REPOALTIPATH}" != "${IPATH}" -a "${FORGEALTIPATH}" != "${REPOALTIPATH}" ]; then
        ALTIPATHS+=" ${REPOALTIPATH}"
    fi
    ALTIPATHS=$(echo ${ALTIPATHS} | sed -e 's/^ //g')

    GITFILE=$(mktemp)
    git ls-remote ${FORGE} > ${GITFILE}
    GITREFS=$(grep -P "\trefs/tags/${DVERSION}$" ${GITFILE})
    GITENTS=$(echo ${GITREFS} | wc -w)
    if [ ${GITENTS} -lt 2 ]; then
        GITREFS=$(grep -P "\tHEAD$" ${GITFILE})
    elif [ ${GITENTS} -gt 2 ]; then
        echo "TOO MANY VERSIONS:"
        echo "${GITREFS}"
        exit 1
    fi
    GITENTS=$(echo ${GITREFS} | wc -w)
    if [ ${GITENTS} -ne 2 ]; then
        echo "INVALID VERSION:"
        cat ${GITFILE}
        exit 1
    fi
    COMMIT=$(echo ${GITREFS} | awk '{print $1}')
    TAGREF=$(echo ${GITREFS} | awk '{print $2}')

    for D in MOD GOIMPORT ROOTPATH VCS REPOURL ROOTSUBDIR PKGGODEVURL DVERSION DMODPATH DPKGPATH DTYPE SUBDIR FORGE IPATH ALTIPATHS VERSION TAG COMMIT TYPE; do
        echo "${D}: ${!D}"
    done

    if [ "${TAG}" == "v${VERSION}" ]; then
        TAG=""
        COMMIT=""
    fi

    grep -q -P "^${IPATH},${FORGE},.*" goipaths.txt
    if [ $? -ne 0 -a "${SUBDIR}" == "" ]; then
        LINE="${IPATH},${FORGE},${SUBDIR},${ALTIPATHS},${VERSION},${TAG},${COMMIT},${SRCTGZ},${DSTTGZ},${TYPE}"
        echo -n "ENTRY: "
        echo "${LINE}" | tee -a goipaths.txt

        DESCRIPTION=$(cat ${PKGGODEVFILE} | grep -A 1000 'Documentation-overviewHeader' | grep -m 1 -B 100 '^</p>'  | grep -A 100 '^<p>' | tidy 2>/dev/null | lynx -dump -nolist -stdin | sed -e 's/^   //g' | tr '\n' ' ' | sed -e 's/,/\&#44;/g')
        SUMMARY=$(echo ${DESCRIPTION} | cut -d\. -f1)
        DOCS="${IPATH},${SUMMARY},${DESCRIPTION}"
        echo -n "DOCS: "
        echo "${DOCS}" | sed -e 's/\ $//g' | tee -a goipaths-docs.txt
    fi

    rm ${PKGGODEVFILE} ${GITFILE}
    echo "=========== END ${MOD} ==========="
done
