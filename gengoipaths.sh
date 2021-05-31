#! /bin/bash

echo "#IPATH,FORGE,SUBDIR,ALTIPATHS,VERSION,TAG,COMMIT,SRCTGZ,DSTTGZ" > goipaths.txt

declare -A FPATHOVERRIDE

FPATHOVERRIDE['code.google.com/p/go-uuid/uuid']='https://github.com/pborman/uuid'

for PKG in $(cat packages.txt); do
    echo ${PKG}
    TMPFILE=$(mktemp)
    curl -s https://pkg.go.dev/${PKG} > ${TMPFILE}
    FPATH=$(grep -A 7 Repository ${TMPFILE} | grep -P -o '<a href=".*" ' | cut -d\" -f2 | grep -P -o "https:\/\/.*")
    if [ "${FPATH}" == "" ]; then
        FPATH=${FPATHOVERRIDE[${PKG}]}
    fi
    if [ "${FPATH}" == "" ]; then
        echo "Cannot determine FPATH for ${PKG}"
        exit 1
    fi
    TAG=$(grep -P 'data-version=".*"' ${TMPFILE} | head -1 | cut -d\" -f2)
    echo "${TAG}" | grep '-'
    if [ $? -eq 0 -o "${TAG}" == "" ]; then
        TAG=$(git ls-remote ${FPATH}.git | grep -v '-' | grep -v '\^{}$' | tail -1 | rev | cut -d\/ -f1 | rev)
    fi
    VERSION=""
    COMMIT=""
    echo ${TAG} | grep '^v'
    if [ $? -eq 0 ]; then
        VERSION=$(echo -n ${TAG} | sed -e 's/^v//g')
            TAG=""
    else
        COMMIT=$(git ls-remote ${FPATH}.git refs/tags/${TAG} | awk '{print $1}')
    fi
    echo ${TAG} | grep '\.'
    if [ $? -ne 0 -a "${TAG}" != "" ]; then
        COMMIT=$(git ls-remote ${FPATH}.git HEAD | awk '{print $1}')
        TAG=""
    fi
    MPATH=$(grep -P 'data-mpath=".*"' ${TMPFILE} | head -1 | cut -d\" -f2)
    if [ "${MPATH}" == "" ]; then
        MPATH=${PKG}
    fi
    PPATH=$(grep -P 'data-ppath=".*"' ${TMPFILE} | head -1 | cut -d\" -f2)
    if [ "${PPATH}" == "" ]; then
        PPATH=${PKG}
    fi
    echo "${VERSION} - ${MPATH} - ${PPATH} - ${FPATH}"
    grep "^${MPATH}," goipaths.txt
    if [ $? -ne 0 ]; then
        echo "${VERSION}" | grep '-'
        if [ $? -eq 0 ]; then
            VERSION=$(git ls-remote ${FPATH}.git | grep -v '-' | grep -v '\^{}$' | tail -1 | rev | cut -d\/ -f1 | rev | sed -e 's/^v//g')
        fi
        echo "${MPATH},${FPATH},,,${VERSION},${TAG},${COMMIT},," >> goipaths.txt
    fi
    rm ${TMPFILE}
done

