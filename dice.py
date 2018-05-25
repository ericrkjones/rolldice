#!/usr/bin/python
import re
from random import randint as randint
itermax=1000

def roll(N,sides):
	output = [randint(1,sides) for n in range(0,N)]
	# print(output)
	return output

def evaldice(matchobj):
	rolled = sorted(roll(int(matchobj.group(1)),int(matchobj.group(2))))
	if matchobj.group(3) == 'l':
		result = rolled[int(matchobj.group(4)):]
		# print "Dropped lowest", matchobj.group(4), "dice:", rolled, '>', result
	else:
		if matchobj.group(3) == 'h':
			result = rolled[:-int(matchobj.group(4))]
			# print "Dropped highest", matchobj.group(4), "dice:", rolled, '>', result
		else:
			result = rolled


	total = str(sum(result))
	# print 'Rolling:', matchobj.groups(), '=', total
	return total

def evaluatedicelist(matchobj):
	# print 'inside parentheses -', matchobj.group(0)
	# print matchobj.group(1)
	new = re.sub('([0-9]+)d([0-9]+)(?:(l|h)([0-9]+))?', evaldice, matchobj.group(1))
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
