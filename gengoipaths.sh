#! /bin/bash

echo "#IPATH,FORGE,SUBDIR,ALTIPATHS,VERSION,TAG,COMMIT,SRCTGZ,DSTTGZ,TYPE" > goipaths.txt
echo "#IPATH,SUMMARY,DESCRIPTION" > goipaths-docs.txt

for IPATH in $(cat packages.txt); do
    echo "========== BEGIN ${IPATH} =========="
    echo "IPATH: ${IPATH}"

    INAME=$(basename $(echo "${IPATH}" | sed -e 's/\/v[0-9]\+$//g'))
    echo "INAME: ${INAME}"

    PKGGODEVFILE=$(mktemp)
    URL="https://pkg.go.dev/${IPATH}"
    echo "URL: ${URL}"

    curl -s ${URL} > ${PKGGODEVFILE}
    FPATH=$(grep -A 7 Repository ${PKGGODEVFILE} | grep -P -o '<a href=".*" ' | cut -d\" -f2 | grep -P -o "https:\/\/.*")
    DVERSION=$(grep -P 'data-version=".*"' ${PKGGODEVFILE} | head -1 | cut -d\" -f2 | sed -e 's/\+incompatible//g')
    DMODPATH=$(grep -P 'data-mpath=".*"' ${PKGGODEVFILE} | head -1 | cut -d\" -f2)
    DPKGPATH=$(grep -P 'data-ppath=".*"' ${PKGGODEVFILE} | head -1 | cut -d\" -f2)
    DTYPE=$(grep -P 'data-pagetype=".*"' ${PKGGODEVFILE} | head -1 | cut -d\" -f2)
    if [ "${FPATH}" == "" ]; then
        echo "Cannot find FPATH"
        FPATH="https://${IPATH}"
        DMODPATH=${IPATH}
        DPKGPATH=${IPATH}
    fi
    ALTIPATHS=""
    ALTIPATH=$(echo "${FPATH}" | sed -e 's/^https:\/\///g')
    if [ "${ALTIPATH}" != "${DMODPATH}" ]; then
        ALTIPATHS=${ALTIPATH}
    fi
    FNAME=$(basename $(echo "${FPATH}" | sed -e 's/\/v[0-9]\+$//g'))
    MNAME=$(basename $(echo "${DMODPATH}" | sed -e 's/\/v[0-9]\+$//g'))
    PNAME=$(basename $(echo "${DPKGPATH}" | sed -e 's/\/v[0-9]\+$//g'))
    for D in FPATH FNAME DVERSION DMODPATH MNAME DPKGPATH PNAME DTYPE; do
        echo "${D}: ${!D}"
    done

    grep "^${DMODPATH}," goipaths.txt
    if [ $? -eq 0 ]; then
        echo -n "EXISTS: "
        grep "^${DMODPATH}," goipaths.txt
        continue
    fi

    grep "^${DMODPATH}," goipaths-overrides.txt
    if [ $? -eq 0 ]; then
        echo -n "OVERRIDE: "
        LINE=$(grep "^${DMODPATH}," goipaths-overrides.txt)
        echo "${LINE}" | tee -a goipaths.txt
        continue
    fi

    VERSION=$(echo ${DVERSION} | sed -e 's/^v//g')
    echo "VERSION: ${VERSION}"

    GITLSFILE=$(mktemp)
    git ls-remote ${FPATH}.git > ${GITLSFILE}
    if [ $? -ne 0 ]; then
        echo "Problem retrieving remote list of ${FPATH}.git"
        continue
    fi

    TAG="${INAME}/${DVERSION}"
    LINE=$(grep -P ".*\srefs/tags/${TAG}$" ${GITLSFILE})
    if [ $? -ne 0 ]; then
        LINE=$(grep -P ".*\srefs/heads/${TAG}$" ${GITLSFILE})
    fi
    WORDS=$(echo ${LINE} | wc -w)
    if [ ${WORDS} -lt 2 ]; then
        TAG="${FNAME}/${DVERSION}"
        LINE=$(grep -P ".*\srefs/tags/${TAG}$" ${GITLSFILE})
        if [ $? -ne 0 ]; then
            LINE=$(grep -P ".*\srefs/heads/${TAG}$" ${GITLSFILE})
        fi
        WORDS=$(echo ${LINE} | wc -w)
        if [ ${WORDS} -lt 2 ]; then
            TAG="${MNAME}/${DVERSION}"
            LINE=$(grep -P ".*\srefs/tags/${TAG}$" ${GITLSFILE})
            if [ $? -ne 0 ]; then
                LINE=$(grep -P ".*\srefs/heads/${TAG}$" ${GITLSFILE})
            fi
            WORDS=$(echo ${LINE} | wc -w)
            if [ ${WORDS} -lt 2 ]; then
                TAG="${PNAME}/${DVERSION}"
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
                            echo "Invalid TAG: ${TAG}"
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
            elif [ ${WORDS} -gt 2 ]; then
                echo "Found too many entries:"
                echo ${WORDS}
                exit 1
            else
                VERSION=""
                COMMIT=$(echo ${LINE} | awk '{print $1}')
            fi
        elif [ ${WORDS} -gt 2 ]; then
            echo "Found too many entries:"
            echo ${WORDS}
            exit 1
        else
            VERSION=""
            COMMIT=$(echo ${LINE} | awk '{print $1}')
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

    LINE="${DMODPATH},${FPATH},,${ALTIPATHS},${VERSION},${TAG},${COMMIT},,,${DTYPE}"
    echo -n "ENTRY: "
    echo "${LINE}" | tee -a goipaths.txt

    DESCRIPTION=$(cat ${PKGGODEVFILE} | grep -A 1000 'Documentation-overviewHeader' | grep -m 1 -B 100 '^</p>'  | grep -A 100 '^<p>' | tidy 2>/dev/null | lynx -dump -nolist -stdin | sed -e 's/^   //g' | tr '\n' ' ' | sed -e 's/,/\&#44;/g')
    SUMMARY=$(echo ${DESCRIPTION} | cut -d\. -f1)
    DOCS="${DMODPATH},${SUMMARY},${DESCRIPTION}"
    echo -n "DOCS: "
    echo "${DOCS}" | tee -a goipaths-docs.txt

    rm ${PKGGODEVFILE} ${GITLSFILE}
    echo "=========== END ${IPATH} ==========="
done
