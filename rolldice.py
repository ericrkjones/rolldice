#!/usr/bin/python
# Argument list is a comma-separated list of lists of dice expressions and names
# For example: ./rolldice.py '(1d4*2)d6 karate chickens, 2d6d8'

import sys
import re
from dice import dicelist as dicelist
from dice import roll as roll

def parseinstructions(strargs):
	instructions=[x.split(' ',1) for x in re.split(', *',strargs)]
	print instructions
	for item in instructions:
		rollednumber = dicelist(item[0])
		if len(item) > 1:
			print "{} {}".format(rollednumber, item[1])
		else:
			print "{}".format(rollednumber)

parseinstructions(' '.join(sys.argv[1:]))

