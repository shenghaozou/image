import subprocess
import time
import json
import sys

result = []
log = sys.argv[1]
for i in range(int(sys.argv[2])):
    start_time = time.time()
    r = subprocess.check_output(
        "{} {};exit 0".format(sys.argv[3], sys.argv[4]),
        stderr=subprocess.STDOUT,
        shell=True)
    e_time = time.time() - start_time
    result.append(str(e_time))

with open(log, "w") as fw:
    fw.write(json.dumps(result))

print("RESULT:", result)
