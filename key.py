from evdev import InputDevice
from select import select
import time
import thread

def recent_keypress_count():
    return len(times)

def expire():
    while True:
        f = open('keypress_count','w')
        if not len(times) == 0:
            f.write(str(recent_keypress_count()))
        else:
            f.write('0')
        f.close()
        time.sleep(0.1)
        for t in list(times):
            if time.time()-t > 60:
               times.remove(t)

dev = InputDevice('/dev/input/event0')

times = set()
thread.start_new_thread(expire,())

while True:
   r,w,x = select([dev], [], [])
   for event in dev.read():
#       print(len(times))
       times.add(time.time())

# event at 1337427573.061822, code 01, type 02, val 01
# event at 1337427573.061846, code 00, type 00, val 00
