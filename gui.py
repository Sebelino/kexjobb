#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  namnlös.py
#  
#  Copyright 2013 Jonatan Åkesson <jonatan@cbbb>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import time
import os
import subprocess
import re
from threading import Thread

def kod():
	s = ''
	bl = '3000'
	s = get_active_window_title("")

	print("" + s)

	if s.find('Zenia') > 0:
		bl= '3500'
	elif s.find('Hej') > 0:
		print("Hittade Chrome!")
		bl= '100'
	elif s.find('Kate') > 0:
		bl='5'
	elif s.find('Chrom') > 0:
		bl='2000'
	elif s.find('no') > 0:
		bl='500'
		
	#sätter brightness
	p1 = subprocess.Popen(['echo', bl], stdout=subprocess.PIPE)
	#p2 = subprocess.Popen(['tee', '/sys/class/backlight/intel_backlight/brightness'], stdin=p1.stdout)
	p2 = subprocess.Popen(['tee', '/sys/class/backlight/acpi_video0/brightness'], stdin=p1.stdout)
	p1.stdout.close() 
	output = p2.communicate()
	
	
	
	#läser actual brightness
	actual_bright = ''
	p3 = subprocess.Popen(['cat', '/sys/class/backlight/acpi_video0/brightness'], stdout=subprocess.PIPE)
	#p3 = subprocess.Popen(['cat', '/sys/class/backlight/intel_backlight/brightness'], stdout=subprocess.PIPE)
	for line in p3.stdout:
	  actual_bright = line.rstrip()
	  print("actual brightness: " + line)
	  
	
	#read keypresses
	#
	key_presses = "33"
	#
	
	
	
	# skriver till fil klassifieringsfil
	
	skriv = "" + key_presses + ",?,"  + actual_bright + ",?,?,lower." 
	f = open('power.test','w')
	f.write("")
	f.write(skriv)
	f.close()
	
	
	
	
	#Klassifierar med adaboost
	lista = boost()
	print(lista)
	
	
	
	#höjer eller sänker
	#sätter brightness
	#p1 = subprocess.Popen(['echo', bl], stdout=subprocess.PIPE)
	#p2 = subprocess.Popen(['tee', '/sys/class/backlight/intel_backlight/brightness'], stdin=p1.stdout)
	#p2 = subprocess.Popen(['tee', '/sys/class/backlight/acpi_video0/brightness'], stdin=p1.stdout)
	#p1.stdout.close() 
	#output = p2.communicate()
	
	
	time.sleep(0.5)




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
	rad = read.readline()
	lista = rad.split(" ")
	return lista
	
	
while 1==1:
  kod()
 
root.mainloop()
