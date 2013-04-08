import os

command = "sudo cat /sys/class/backlight/intel_backlight/brightness"

os.system(command)
