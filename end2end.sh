#! /bin/bash

touch end2end.log end2end.txt

FILES=$(ls -1 *.log *.txt | tr '\n' ' ')
echo "Cleaning ${FILES}..."

for FILE in ${FILES}; do
    echo -n "Reset ${FILE}... "
    rm -fv ${FILE}
    touch ${FILE}
done

echo "Removing mock-chain-root temporary directories..."
rm -rfv /var/tmp/mock-chain-root-*-* 2>&1 | tee end2end.log
mktemp -d -p /var/tmp mock-chain-root-$$-XXXXXXXX 2>&1 | tee -a end2end.log

echo "Restoring goipaths-gometa.txt goipaths-overrides.txt..."
git restore goipaths-gometa.txt goipaths-overrides.txt 2>&1 | tee -a end2end.log

echo "Initialize end2end.txt and packages.txt..."
DIFF=1
PASS=0
echo "${PASS}" | tee end2end.log
touch end2end-{curr,prev}.log
echo "github.com/haproxytech/haproxy-consul-connect" | tee packages.txt | tee -a end2end.log

while [ ${DIFF} -ne 0 ]; do
    echo "in loop"
    let PASS=${PASS}+1
    echo "${PASS}" | tee end2end.log | tee -a end2end.log

    ./genbuild.sh

    git status | tee -a end2end.log
    git diff | tee -a end2end.log
    grep -r Traceback $(ls -ctrad /var/tmp/mock-chain-root-* | tail -1) | tee -a end2end.log

    UNTRACKED=$(git status | grep -A 1000 ' to include in what will be committed' | grep -v ' to include in what will be committed' | grep -v '^no changes added to commit ' | tr '\n' ' ')
    if [ "${UNTRACKED}" != "" ]; then
        git add ${UNTRACKED} | tee -a end2end.log
    fi

    MODIFIED=$(git status | grep -P '^\t.*:\s+' | grep -P -v '\tdeleted:\s+' | cut -d\: -f2 | tr '\n' ' ')
    if [ "${MODIFIED}" != "" ]; then
        git commit -m "pass ${PASS}" ${MODIFIED} | tee -a end2end.log
    fi

    mv -v end2end-{curr,prev}.log
    wc *.txt | tee end2end-curr.log
    diff -u end2end-{curr,prev}.log
    DIFF=$?
done
