#! /bin/bash

set -euf -o pipefail

./genpackages.sh 2>&1 | tee genpackages.log
 
./gengoipaths.sh 2>&1 | tee gengoipaths.log

./gengocheck.sh 2>&1 | tee gengocheck.log

./gengometa.sh 2>&1 | tee gengometa.log

./build.sh

