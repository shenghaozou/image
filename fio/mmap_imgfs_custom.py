import sys
if (sys.version_info > (3, 0)):
    p = '/img/package3.7'
else:
    p = '/img/package'

sys.path = [p] + sys.path
import time
start = time.time()
import numpy as np
import scipy
import requests
import matplotlib
import nltk
import sympy
end = time.time()
print(end - start)
