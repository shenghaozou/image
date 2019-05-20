#!/usr/bin/env python3

import re
import json
import sys
import os
reg = "READ: bw=[\d\.]*MiB\/s \(([\d\.]*)MB"
reg_kb = "READ: bw=[\d\.]*KiB\/s \(([\d\.]*)kB"

fn = sys.argv[1]

with open(fn) as fr:
    f = fr.read()
r = re.findall(reg, f)
if len(r) == 0:
    r = re.findall(reg_kb, f)
    r = [str(float(x)/1024.0) for x in r]
data = json.dumps(r)
print(data)

if len(sys.argv) > 2:
    folder = sys.argv[2]
    objname = os.path.join(folder, fn.replace(".log", ".json"))
    with open(objname, "w") as fw:
        fw.write(data)
    print("data written to ", objname)

s = 0
for i in r:
    s += float(i)
print("AVG for {} : {}".format(sys.argv[1], float(s)/len(r)))
