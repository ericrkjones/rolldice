#!/usr/bin/python3
import sys
import re
from discreteprobabilitydistribution import Distribution
from random import randint as randint
from dice import interpretinstructions, dropdice
import matplotlib.pyplot as plt

# Iterate every potential rolled set, drop dice, and populate a distribution.
def comprehensiveIterateModel(N,d,drop,dropN):
	if isinstance(N, int):
		new = Distribution()
		new.populateIndividualChoice(N)
		N = new.normalize()
	# print(N.distribution)
	distribution = Distribution()
	for x in N.distribution:
		rolled = [1 for x in range(x)]
		numberofchoices=d**x
		each=N.distribution[x]/numberofchoices
		for n in range(numberofchoices):
			distribution.populateIndividualChoice(sum(dropdice(rolled, drop, dropN)), count=each)
			rolled[0] += 1
			for index in range(x):
				if rolled[index] > d:
					rolled[index] = 1
					if index + 1 < x:
						rolled[index+1] +=1
	print(distribution.distribution)
	return distribution					

# Random number generated roll.  
def roll(N,d,drop,Ndrop):
	output = comprehensiveIterateModel(N,d,drop,Ndrop)
	return output

# Parse instructions for rolling random numbers and displaying them in the output
def parseinstructions(strargs):
	instructions=[x.split(' ',1) for x in re.split(', *',strargs)]
	print(instructions)
	for item in instructions:
		interpreted = interpretinstructions(item[0])
		print(interpreted)
		rolled = eval(interpreted)
		formatted = rolled.plotformat()
		plt.plot(formatted[0], formatted[1])
		plt.title(item[1])
		plt.show()

parseinstructions(' '.join(sys.argv[1:]))


