#!/bin/bash

echo "Tests running"

echo "run ../testCaseExecutables/TestSh.sh "

./testCaseExecutables/TestSh.sh
echo ""
echo ""
echo ""

echo "For Loop"
echo ""
for filename in testCases/*.txt; do
	echo "$filename"

done
echo ""
echo ""
echo ""
echo "Running Python"
echo ""

python ./testCaseExecutables/testCase1.py


echo "done"
