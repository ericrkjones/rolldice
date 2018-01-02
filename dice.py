#!/usr/bin/python
import re
from random import randint as randint
itermax=1000

def roll(N,sides):
	return sum([randint(1,sides) for n in range(0,N)])

def evaldice(matchobj):
	result = str(roll(int(matchobj.group(1)),int(matchobj.group(2))))
	# print 'Rolling:', matchobj.group(0), '=', result
	return result

def evaluatedicelist(matchobj):
	# print 'inside parentheses -', matchobj.group(0)
	new = re.sub('([0-9]+)d([0-9]+)', evaldice, matchobj.group(1))
	result=str(eval(new))
	# print 'Evaluating: ', new, '=', result
	return result

def evaluateparentheses(matchobj):
	# print 'new level: ', matchobj.group(1)
	return re.sub('\(([^()]*)\)', evaluatedicelist, matchobj.group(1))
	
def dicelist(strarg):
	# Create a count variable to limit overrunning
	count = 0
	# Parse everything in parentheses.  
	# As long as there are parentheses in the dice list, evaluate all discrete inner-most parentheses
	while count < itermax and '(' in strarg or ')' in strarg:
		# print 'Level', count, ':'
		strarg = re.sub('(.*)', evaluateparentheses, strarg)
		count += 1
	strarg = re.sub('(.*)', evaluatedicelist, strarg)
	return strarg
