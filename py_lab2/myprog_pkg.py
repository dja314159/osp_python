#!/usr/bin/python3

import sys
import re

from my_pkg import bin
from my_pkg import set


while True:
	num =int( input("Select menu: 1)conversion 2)union/intersection 3)exit? "))

	if num==1:
		bin.binToOther()
	elif num==2:
		set.setCal()
	elif num==3:
		print("exit program...")
		break
