#! /bin/bash

for i in $(grep '^No matching package to install: ' build.log  | cut -d\( -f2 | cut -d\) -f1); do
    grep ^${i}$ packages.txt
    if [ $? -ne 0 ]; then
        echo ${i} >> packages.txt
    fi
done
