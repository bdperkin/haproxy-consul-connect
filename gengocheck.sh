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

#grep -P -r '^FAIL\t' $(ls -ctrad /var/tmp/mock-chain-root-* | tail -1) > ${FAILLOG}
LOGS=$(grep -P -r '^error: ' /var/tmp/mock-chain-root-* | grep ' (%check)$' | cut -d: -f1 | uniq)

for LOG in ${LOGS}; do
    grep -A2 '^      testing: ' ${LOG} | grep -B2 -E "( expects import | cannot find package )" | grep -v '^--$' | grep -A1 '^      testing: ' | tr '\n' ' ' | sed -e 's/      testing: /\n/g' | sed -e 's/\ $//g' | sed -e 's/ --$//g'
done | sort -u | grep -v '^$' > ${FAILLOG}

awk '{print $1}' ${FAILLOG} > ${FAILLIST}
cp /dev/null ${REGEXPS}
for TEST in $(awk '{print $2}' ${FAILLOG}); do
    echo "$(basename ${TEST} | cut -d\. -f1)" >> ${REGEXPS}
done

paste ${FAILLIST} ${REGEXPS} >> ${PASTE}
cat ${PASTE}

for IPATH in $(cut -d, -f1 goipaths.txt); do
        REGEXP=$(grep "^${IPATH}" ${PASTE} | awk '{print $2}')
        if [ "${REGEXP}" != "" ]; then
                LINE="${IPATH},%gocheck"
                for R in ${REGEXP}; do
                        LINE+=" -r .*${R}.*"
                done
                echo "${LINE}" >> goipaths-gocheck.txt
        fi
done

rm ${FAILLOG} ${FAILLIST} ${REGEXPS} ${PASTE}
