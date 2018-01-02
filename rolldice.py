#!/usr/bin/python
# Arguments are dice expressions separated by 

import sys
import re
from dice import dicelist as dicelist
from dice import roll as roll

def parseinstructions(strargs):
	instructions=[x.split(' ',1) for x in re.split(', *',strargs)]
	print instructions
	for item in instructions:
		rollednumber=dicelist(item[0])
		print "{} {}".format(rollednumber, item[1])
	return instructions

parseinstructions(' '.join(sys.argv[1:]))

