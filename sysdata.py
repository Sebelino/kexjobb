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
    read = os.popen("cat /sys/class/power_supply/BAT0/energy_now")
    read2 = os.popen("cat /sys/class/power_supply/BAT0/energy_full")
    charge_now = float(read.readline())
    charge_full = float(read2.readline())
    bat_percent = str(100*charge_now/charge_full)
    
    # läser använt minne
    read3 = os.popen("free")
    read3.readline()
    mem = read3.readline()
    
    mem_list = mem.split(" ")
    total = float(re.sub("[^0-9]", "",str(mem_list[7])))
    used = float(re.sub("[^0-9]", "",str(mem_list[11])))
    free = float(re.sub("[^0-9]", "",str(mem_list[15])))
    buffers = float(re.sub("[^0-9]", "",str(mem_list[25])))
    cached = float(re.sub("[^0-9]", "",str(mem_list[31])))
    mem_used_percent = 100*(used - cached -buffers)/total
    
    #läser average load
    read4 = os.popen("uptime")
    cpu = read4.readline()
    cpu_list = cpu.split(", ")
    up1= 0.01*int(re.sub("[^0-9]", "",str(cpu_list[2])))
    up2= 0.01*int(re.sub("[^0-9]", "",str(cpu_list[3])))
    up3= 0.01*int(re.sub("[^0-9]", "",str(cpu_list[4])))

    plugged = os.popen("cat /sys/class/power_supply/AC0/online")
    plugged_in = bool(int(plugged.readline()))

    return bat_percent,mem_used_percent,up1,up2,up3,plugged_in

