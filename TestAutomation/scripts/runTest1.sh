#!/bin/bash
# Script for testing
clear
sleep 1
cd ../project/Jython/
result=$(sh ./jython.sh -i library/test1.py "startTest" 2>&1)
echo "\nResult:"
echo "$result"
echo "\nResult 2:"
echo "$result"
