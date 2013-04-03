#!/usr/bin/python
import sys
import atexit
import time
global count
global fname
 
fname = 'keycount'
def savecounter():
	f = open(fname,'w')
	f.write(str(count))
	f.write('\n')
	f.close()
 
atexit.register(savecounter)
f = open(fname,'r')
count = int(f.readline()
f.close()
 
t = time.time()
input = open("/dev/input/event"+sys.argv[1],'rb')
while True:
	input.read(96)
	count+=1
	#print(count)
	if (time.time() - t > 60):
		t = time.time()
		savecounter()
