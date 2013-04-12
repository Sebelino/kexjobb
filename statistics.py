import os
import time
import numpy

#powerlist = []
for _ in range(3600):
    int(os.system("cat /sys/class/power_supply/BAT0/power_now | tee -a statistics.txt"))
    #powerlist.append(power)
    time.sleep(1)
