#! /bin/bash

touch build.log

for i in $(grep -P -o 'golang\(.*\)' build.log | sed -e 's/^golang(//g' | sed -e 's/)$//g'); do
    grep ^${i}$ packages.txt
    if [ $? -ne 0 ]; then
        echo ${i} >> packages.txt
    fi
done

CHAINROOT=$(grep -P -o "/var/tmp/mock-chain-root-\d+-.+/results/fedora-rawhide-x86_64$" build.log | uniq)
if [ "${CHAINROOT}" != "" ]; then
    for i in $(grep ': cannot find package "' $(ls -1 ${CHAINROOT}/*/build.log) | cut -d\" -f2); do
        grep ^${i}$ packages.txt
        if [ $? -ne 0 ]; then
            echo ${i} >> packages.txt
        fi
    done
fi
