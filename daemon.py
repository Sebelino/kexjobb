#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os
import subprocess
import re
import thread
from threading import Thread
from constants import MAX_BL

MAX_BL = 4302

os.system("logkeys --start --output keylog.log")

def kod():
    bl = str(MAX_BL)
    s = get_active_window_title("")

    
    #läser actual brightness
    actual_bright = ''
    #p3 = subprocess.Popen(['cat', '/sys/class/backlight/acpi_video0/brightness'], stdout=subprocess.PIPE)
    p3 = subprocess.Popen(['cat', '/sys/class/backlight/intel_backlight/brightness'], stdout=subprocess.PIPE)
    for line in p3.stdout:
      actual_bright = line.rstrip()
    
    #read keypresses
    f = open('keypress_count','r')
    key_presses = f.read()
    f.close()
    if not key_presses:
        print "Nu GICK NAT GALET!!!!!!1111"
        print "Nu GICK NAT GALET!!!!!!1111"
        print "Nu GICK NAT GALET!!!!!!1111"
        print "Nu GICK NAT GALET!!!!!!1111"
        print "Nu GICK NAT GALET!!!!!!1111"
        print "Nu GICK NAT GALET!!!!!!1111"
        print "Nu GICK NAT GALET!!!!!!1111"
        key_presses = "0"
    
    
    # skriver till fil klassifierings
    skriv = "" + key_presses + ","+"?"+","  +str(int(float(actual_bright)/MAX_BL*100)) + ",?,?,lower." 
    f = open('power.test','w')
    f.write("")
    f.write(skriv)
    print(skriv)
    f.close()
    
    
    #Klassifierar med adaboost
    lista = boost()
    #print("lista"+str(lista))
    stay = lista[2]
    higher = lista[3]
    increase = 0
    
    if float(stay) > 0:
        print("")
    elif float(higher) > 0:
        increase = 1
    
    
    #höjer eller sänker
    #sätter brightness
    #
    delta = int(3*0.01*MAX_BL)
    if increase == 1:
          blint = int(actual_bright) + delta
          if blint > MAX_BL:
            bl=str(MAX_BL)
          else:
            bl = str(blint)
          
          
    else:
          blint = int(actual_bright) - delta
          if blint < 0:
            bl="0"
          else:
            bl = str(blint)
    
    p4 = subprocess.Popen(['echo', bl], stdout=subprocess.PIPE)
    p5 = subprocess.Popen(['tee', '/sys/class/backlight/intel_backlight/brightness'], stdin=p4.stdout)
    #p5 = subprocess.Popen(['tee', '/sys/class/backlight/acpi_video0/brightness'], stdin=p4.stdout)
    p4.stdout.close() 
    p5.communicate()
          
    time.sleep(0.1)




def get_active_window_title(self):
    root = subprocess.Popen(['xprop', '-root', '_NET_ACTIVE_WINDOW'], stdout=subprocess.PIPE)

    for line in root.stdout:
        m = re.search('^_NET_ACTIVE_WINDOW.* ([\w]+)$', line)
        if m != None:
            id_ = m.group(1)
            id_w = subprocess.Popen(['xprop', '-id', id_, 'WM_NAME'], stdout=subprocess.PIPE)
            break

    if id_w != None:
        for line in id_w.stdout:
            match = re.match("WM_NAME\(\w+\) = (?P<name>.+)$", line)
            if match != None:
                return match.group("name")

    return "active win no"

def boost():
    lista = []
    read = os.popen("icsiboost -S power -C < power.test; echo $?")
    time.sleep(0.1)
    rad = read.readline()
    lista = rad.split(" ")
    return lista

def keylogger():
    print("start")
    os.system("python key.py")
 

#thread.start_new_thread(keylogger, ())
while 1:
  
  kod()
  
root.mainloop()
