#!/usr/bin/python3
import sys
import re
from random import randint as randint
from dice import interpretinstructions, dropdice

# Random number function as placeholder in case system random is not sufficient.
def randomnumber(low,high):
	return randint(low,high)

# Random number generated roll.  
def roll(N,d,drop,Ndrop):
	output = sum(dropdice([randomnumber(1,d) for n in range(N)],drop,Ndrop))
	return output

# Parse instructions for rolling random numbers and displaying them in the output
def parseinstructions(strargs):
	instructions=[x.split(' ',1) for x in re.split(', *',strargs)]
	print(instructions)
	for item in instructions:
		rolled = eval(interpretinstructions(item[0]))
		if len(item) > 1:
			print(rolled, item[1])
		else:
			print(rolled)

parseinstructions(' '.join(sys.argv[1:]))


