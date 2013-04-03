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
import subprocess
import re
from threading import Thread



level = ""

def kod():
	s = ''
	bl = '3000'
	s = get_active_window_title("")

	print("a" + s)

	if s.find('Hej') > 0:
		print("Hittade Chrome!")
		bl= '10'
	elif s.find('Kate') > 0:
		bl='10'
	elif s.find('Chrom') > 0:
		bl='2000'
	elif s.find('no') > 0:
		bl='500'
		
		
	p1 = subprocess.Popen(['echo', bl], stdout=subprocess.PIPE)
	p2 = subprocess.Popen(['tee', '/sys/class/backlight/intel_backlight/brightness'], stdin=p1.stdout)
	p1.stdout.close() 
	output = p2.communicate()[0]



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


while True:
	time.sleep(2)
	kod()
