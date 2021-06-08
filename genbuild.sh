#! /bin/bash

set -eu

./genpackages.sh 2>&1 | tee genpackages.log
 
./gengoipaths.sh 2>&1 | tee gengoipaths.log

./gengocheck.sh 2>&1 | tee gengocheck.log

./build.sh

