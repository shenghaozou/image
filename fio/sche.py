import sys
import subprocess
import os
import csv
import json
import glob
import time
import shutil 
sche_file = sys.argv[1]
tmp_path = os.path.join("/tmp", sche_file)
cur_time = sche_file + "_" + time.strftime("%H%M%S")
search_path = os.path.join("/tmp", sche_file, "*.json")
rept = sys.argv[2]
print("schedule file:", sche_file, "repeat times:", rept)

shutil.rmtree(tmp_path, ignore_errors = True)
os.mkdir(tmp_path)

with open(sche_file) as fr:
    for name in fr:
        print("execute object: ", name)
        n = name.strip()
        if n == "":
            print("name is empty. PASS")
            continue
        if sche_file.endswith(".sche"):
            subprocess.check_call(["./run_all.sh", rept, n, tmp_path])
        elif sche_file.endswith(".schepy"):
            tokens = n.split(" ")
            subprocess.check_call(["./run_all_py.sh", rept, tokens[0], tokens[1], tmp_path])
        else:
            print("{} is not a valid name".format(n))
    print("DONE!")

all_files = glob.glob(search_path)

fcsv = open(cur_time + ".csv", "w")
fcsv_w = csv.writer(fcsv)

for f in all_files:
    print("FOUND:", f)
    with open(f) as fr:
        data = json.load(fr)
    name = f.replace(".json","")
    row = [os.path.basename(name)] + data
    fcsv_w.writerow(row)

print("CSV generated. ", cur_time)
    
