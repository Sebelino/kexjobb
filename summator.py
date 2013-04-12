import time
import os
import string
import re
from numpy import median
read = os.popen("cat statistics.dat")
for _ in range(120):
    currents = []
    for _ in range(60):
        currents.append(int(read.readline()))
    avg_current = median(currents)
    os.system("echo %s >> statistics_mean.dat"% avg_current)
