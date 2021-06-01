#! /bin/bash

echo "#IPATH,FORGE,SUBDIR,ALTIPATHS,VERSION,TAG,COMMIT,SRCTGZ,DSTTGZ,TYPE" > goipaths.txt

for IPATH in $(cat packages.txt); do
    echo "========== BEGIN ${IPATH} =========="
    echo "IPATH: ${IPATH}"

    NAME=$(basename ${IPATH})
    echo "NAME: ${NAME}"

    PKGGODEVFILE=$(mktemp)
    URL="https://pkg.go.dev/${IPATH}"
    echo "URL: ${URL}"

    curl -s ${URL} > ${PKGGODEVFILE}
    FPATH=$(grep -A 7 Repository ${PKGGODEVFILE} | grep -P -o '<a href=".*" ' | cut -d\" -f2 | grep -P -o "https:\/\/.*")
    if [ "${FPATH}" == "" ]; then
        echo "Cannot find FPATH"
        exit 1
    fi
    echo "FPATH: ${FPATH}"

    DVERSION=$(grep -P 'data-version=".*"' ${PKGGODEVFILE} | head -1 | cut -d\" -f2 | sed -e 's/\+incompatible//g')
    DMODPATH=$(grep -P 'data-mpath=".*"' ${PKGGODEVFILE} | head -1 | cut -d\" -f2)
    DPKGPATH=$(grep -P 'data-ppath=".*"' ${PKGGODEVFILE} | head -1 | cut -d\" -f2)
    DTYPE=$(grep -P 'data-pagetype=".*"' ${PKGGODEVFILE} | head -1 | cut -d\" -f2)
    for D in DVERSION DMODPATH DPKGPATH DTYPE; do
        echo "${D}: ${!D}"
    done

    grep "^${DMODPATH}," goipaths.txt
    if [ $? -eq 0 ]; then
        echo -n "EXISTS: "
        grep "^${DMODPATH}," goipaths.txt
        continue
    fi

    VERSION=$(echo ${DVERSION} | sed -e 's/^v//g')
    echo "VERSION: ${VERSION}"

    GITLSFILE=$(mktemp)
    git ls-remote ${FPATH}.git > ${GITLSFILE}

    TAG="${NAME}/${DVERSION}"
    LINE=$(grep -P ".*\srefs/tags/${TAG}$" ${GITLSFILE})
    if [ $? -ne 0 ]; then
        LINE=$(grep -P ".*\srefs/heads/${TAG}$" ${GITLSFILE})
    fi
    WORDS=$(echo ${LINE} | wc -w)
    if [ ${WORDS} -lt 2 ]; then
        TAG="${DVERSION}"
        LINE=$(grep -P ".*\srefs/tags/${TAG}$" ${GITLSFILE})
        if [ $? -ne 0 ]; then
            LINE=$(grep -P ".*\srefs/heads/${TAG}$" ${GITLSFILE})
        fi
        WORDS=$(echo ${LINE} | wc -w)
        if [ ${WORDS} -lt 2 ]; then
            echo "Cannot find ${DVERSION} tag:"
            cat ${GITLSFILE}
            echo "${DVERSION}" | grep -P "^v0\.0\.0\-\d{14}\-[0-9a-f]{12}$"
            if [ $? -eq 0 ]; then
                LINE=$(grep -P ".*\sHEAD$" ${GITLSFILE})
                WORDS=$(echo ${LINE} | wc -w)
                if [ ${WORDS} -lt 2 ]; then
                    echo "Cannot find HEAD"
                    exit 1
                elif [ ${WORDS} -gt 2 ]; then
                    echo "Found too many entries:"
                    echo ${WORDS}
                    exit 1
                else
                    VERSION=""
                    TAG=""
                    COMMIT=$(echo ${LINE} | awk '{print $1}')
                fi
            else
                echo "Invalid VERSION: ${DVERSION}"
                exit 1
            fi
        elif [ ${WORDS} -gt 2 ]; then
            echo "Found too many entries:"
            echo ${WORDS}
            exit 1
        else
            TAG=""
            COMMIT=""
        fi
    elif [ ${WORDS} -gt 2 ]; then
        echo "Found too many entries:"
        echo ${WORDS}
        exit 1
    else
        VERSION=""
        COMMIT=$(echo ${LINE} | awk '{print $1}')
    fi
    echo "TAG: ${TAG}"
    echo "COMMIT: ${COMMIT}"

    LINE="${DMODPATH},${FPATH},,,${VERSION},${TAG},${COMMIT},,,${DTYPE}"
    echo -n "ENTRY: "
    echo "${LINE}" | tee -a goipaths.txt

    rm ${PKGGODEVFILE} ${GITLSFILE}
    echo "=========== END ${IPATH} ==========="
done
