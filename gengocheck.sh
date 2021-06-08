#! /bin/bash

cp /dev/null goipaths-gocheck.txt

FAILLOG=$(mktemp)
FAILLIST=$(mktemp)
REGEXPS=$(mktemp)
PASTE=$(mktemp)

#grep -P -r '^FAIL\t' $(ls -ctrad /var/tmp/mock-chain-root-* | tail -1) > ${FAILLOG}
grep -P -r '^FAIL\t' /var/tmp/mock-chain-root-* > ${FAILLOG}
awk '{print $2}' ${FAILLOG} | sort -u > ${FAILLIST}
for TEST in $(cat ${FAILLIST}); do
        echo "$(basename ${TEST} | cut -d\. -f1)" >> ${REGEXPS}
done

paste ${FAILLIST} ${REGEXPS} > ${PASTE}

for IPATH in $(cut -d, -f1 goipaths.txt); do
        REGEXP=$(grep "^${IPATH}" ${PASTE} | awk '{print $2}')
        if [ "${REGEXP}" != "" ]; then
                LINE="${IPATH},%gocheck"
                for R in ${REGEXP}; do
                        LINE+=" -r .*${REGEXP}.*"
                done
                echo "${LINE}" >> goipaths-gocheck.txt
        fi
done

rm ${FAILLOG} ${FAILLIST} ${REGEXPS} ${PASTE}
