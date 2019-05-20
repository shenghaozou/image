#!/bin/sh
for i in $(eval echo {1..$1});
do
	echo "test: $i\n"
	fio $2.fio
done
