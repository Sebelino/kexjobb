#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  namnlös.py
#  
#  Copyright 2013 Jonatan <jonatan@msi>
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
import string
import re

def sysdata():
	# läser batteridata
	read = os.popen("cat /sys/class/power_supply/BAT1/charge_now")
	read2 = os.popen("cat /sys/class/power_supply/BAT1/charge_full")
	charge_now = float(read.readline())
	charge_full = float(read2.readline())
	bat_percent = str(100*charge_now/charge_full)
	
	# läser använt minne
	read3 = os.popen("free")
	read3.readline()
	mem = read3.readline()
	
	mem_list = mem.split(" ")
	total = float(re.sub("[^0-9]", "",str(mem_list[7:8])))
	used = float(re.sub("[^0-9]", "",str(mem_list[12:13])))
	free = float(re.sub("[^0-9]", "",str(mem_list[17:18])))
	buffers = float(re.sub("[^0-9]", "",str(mem_list[33:34])))
	cached = float(re.sub("[^0-9]", "",str(mem_list[38:39])))
	mem_used_percent = 100*(used - cached -buffers)/total
	
	#läser average load
	read4 = os.popen("uptime")
	cpu = read4.readline()
	cpu_list = cpu.split(", ")
	up1= re.sub("[^0-9]", "",str(cpu_list[2]))
	up2= re.sub("[^0-9]", "",str(cpu_list[3]))
	up3= re.sub("[^0-9]", "",str(cpu_list[4]))
	
	return bat_percent,mem_used_percent,up1,up2,up3

