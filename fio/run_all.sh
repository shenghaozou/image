#!/bin/sh
echo "Running test $1 times with test file $2.fio\n"
rm $2.log
bash run.sh $1 $2 >> $2.log
python read_result.py $2.log $3
