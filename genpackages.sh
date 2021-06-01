#! /bin/bash

for i in $(grep '^No matching package to install: ' build.log  | cut -d\( -f2 | cut -d\) -f1); do
    grep ^${i}$ packages.txt
    if [ $? -ne 0 ]; then
        echo ${i} >> packages.txt
    fi
done

CHAINROOT=$(grep -P -o "/var/tmp/mock-chain-root-\d+-.+/results/fedora-rawhide-x86_64$" build.log)
for i in $(grep ': cannot find package "' ${CHAINROOT}/*/build.log | cut -d\" -f2); do
    grep ^${i}$ packages.txt
    if [ $? -ne 0 ]; then
        echo ${i} >> packages.txt
    fi
done
