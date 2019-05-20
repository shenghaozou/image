#!/bin/sh
echo "Running test $1 times with test command $2 $3"
log="$4/$2_$3.json"
echo "LOG location: $log"
python3 run_py_test.py $log $1 $2 $3
