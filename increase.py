import os,sys
import subprocess
import constants

p3 = subprocess.Popen(['cat', '/sys/class/backlight/intel_backlight/brightness'], stdout=subprocess.PIPE)
for line in p3.stdout:
    actual_bright = int(line.rstrip())

brightness = actual_bright+constants.DIFFERENCE

command = "echo %s | sudo tee /sys/class/backlight/intel_backlight/brightness"% brightness

os.system(command)
