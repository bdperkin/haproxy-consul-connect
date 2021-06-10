#! /bin/bash

TMPFILE=$(mktemp)

for IPATH in $(cut -d, -f1 goipaths.txt); do
    grep "^${IPATH}," goipaths-gometa.txt >> ${TMPFILE}
done

if [ "$(wc goipaths-gometa.txt | awk '{print $1,$2,$3}')" != "$(wc ${TMPFILE} | awk '{print $1,$2,$3}')" ]; then
    echo "Something is wrong between goipaths-gometa.txt and ${TMPFILE}."
    diff -u goipaths-gometa.txt ${TMPFILE}
    exit 1
else
    mv ${TMPFILE} goipaths-gometa.txt
fi

