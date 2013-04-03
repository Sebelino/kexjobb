#!/usr/bin/python

import thread
import time
from evdev import InputDevice
from select import select
import time
from multiprocessing import Process


a = -3

def print_time( threadName, delay):
   global a
   if threadName == "Thread-1":
      start = time.time()
      while 1:
	  if time.time() - start >= 5:
	    start = time.time()
	    print(a/6)
	    a=0
   else:
     dev = InputDevice('/dev/input/event0')
     r,w,x = select([dev], [], [])
     while 1:
      for event in dev.read():
	a = a + 1

try:
   thread.start_new_thread( print_time, ("Thread-1", 2, ) )
   thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
   print "Error: unable to start thread"

while 1:
   pass
 
 
 #11111111111