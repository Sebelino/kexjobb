#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os
import subprocess
import re
import thread
from threading import Thread
from constants import MAX_BL
from constants import TRAIN_DELAY
from constants import DIM_PERCENT

def initialize():
    os.system("python2 key.py &")
    os.system("logkeys -k")
    open("keylog.log","w").close() # Empties the file.
    os.system("logkeys --start --output keylog.log")

initialize()
keylog_change = (123,0,0) # (Bytes,number of F5s,number of F6s)
train_delay_counter = -1

def add_entry_decrease(brightness,key_presses):
    entry = "\n%s, ?, %s, ?, ?, lower"%(key_presses,brightness)
    print "Addar detta:             %s"% entry
    with open("power.data","a") as training_set_file:
        training_set_file.write(entry)

def add_entry_increase(brightness,key_presses):
    entry = "\n%s, ?, %s, ?, ?, higher"%(key_presses,brightness)
    print "Addar detta:             %s"% entry
    with open("power.data","a") as training_set_file:
        training_set_file.write(entry)

def confine_training_set():
    rows = file('power.data','r').readlines()
    entry_count = len(filter(None,rows))
    if entry_count >= 20:
        start_index = entry_count-19
        open('power.data','w').writelines(rows[start_index:])

def manual_adjustments(brightness,key_presses):
    global train_delay_counter,keylog_change
    lines = file('keylog.log','r').readlines()
    last_line = lines[-1]
    p = re.compile(r'(<F5>|<F6>)')
    tokens = p.split(last_line)
    current_vals = (os.path.getsize("keylog.log"),
                    len(filter(lambda x: x == "<F5>",tokens)),
                    len(filter(lambda x: x == "<F6>",tokens)))
    if((keylog_change[1] == current_vals[1]) and (keylog_change[2] == current_vals[2])):
        return False
    confine_training_set()
    for token in reversed(tokens):
        if token == '<F6>':
            add_entry_increase(brightness,key_presses)
            break
        elif token == '<F5>':
            add_entry_decrease(brightness,key_presses)
            break
    train_delay_counter = TRAIN_DELAY
    keylog_change = current_vals
    time.sleep(0.3)
    return True

def kod():
    global train_delay_counter,keylog_change
    print "                                   %s"% train_delay_counter
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
        key_presses = "0"

    manual_change = manual_adjustments(str(int(float(actual_bright)/MAX_BL*100)),key_presses)
    if(train_delay_counter == 0):
        os.system("icsiboost -S power -n 10")
        train_delay_counter = -1
    if(manual_change):
        return

    
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
        pass
        #print("")
    elif float(higher) > 0:
        increase = 1
    
    
    #höjer eller sänker
    #sätter brightness
    #
    delta = int(DIM_PERCENT*0.01*MAX_BL)
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

    train_delay_counter -= 1
    if train_delay_counter < 0:
        train_delay_counter = -1
          
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
while 1:
  
    kod()
  
root.mainloop()
