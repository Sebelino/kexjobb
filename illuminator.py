import os,sys

brightness = sys.argv[1]

command = "echo %s | sudo tee /sys/class/backlight/intel_backlight/brightness"% brightness

os.system(command)
