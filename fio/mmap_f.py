import sys
import mmap

f = open(sys.argv[1], "r+b")
mm = mmap.mmap(f.fileno(), 0)
print(mm.readline())
print(len(mm))
print(mm[0])
