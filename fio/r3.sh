rm *.log

bash run_test.sh $1 tmpfs
bash run_test.sh $1 external
