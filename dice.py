import re
# Function to sort the dice roll and remove dice either from the top or bottom.  
def dropdice(rolled, drop, N):
	# If drop or N are None, these are false.
	rolled = sorted(rolled)
	if drop == 'l':
		result = rolled[int(N):]
		# print "Dropped lowest", matchobj.group(4), "dice:", rolled, '>', result
	else:
		if drop == 'h':
			result = rolled[:-int(N)]
			# print "Dropped highest", matchobj.group(4), "dice:", rolled, '>', result
		else:
			result = rolled
	return result

# Translate dice notation 'd' operator into python code
def translatedoperator(matchobj):
	N = matchobj.group(1)
	d = matchobj.group(2)
	drop = matchobj.group(3)
	Ndrop = matchobj.group(4)
	# Function dropdice handles 'None' arguments correctly, so make sure it gets them correctly.
	if drop is None:
		drop = 'None'
	if Ndrop is None:
		Ndrop = 'None'
	return '_[' + N + ',' + d + ',' + drop + ',' + Ndrop + ']'

# Find dice notation expresion and execute replacement with python code
def parseexpression(strarg):
	# print(strarg)
	output = re.sub('([0-9]+|\[.*?\])d([0-9]+|\[.*?\])(?:(l|h)([0-9]+|\[.*?\]))?', translatedoperator, strarg)
	# print(output)
	return output

# Filter instructions to make sure only acceptable characters are present.
def filterinstructions(strarg):
	allowedcharacters = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'd', 'D', 'h', 'H', 'l', 'L', '(', ')', '+', '-', '/', '*', '%', '.')
	if any (x not in allowedcharacters for x in strarg):
		raise ValueError('Disallowed characters in argument string')
	else:
		strarg = strarg.replace(' ', '').lower()
	return strarg

# Translate instructions from dice notation to python code.
def translateinstructions(strarg):
	# Find the highest-level group of parentheses and evaluate it.
	# Relpace the parentheses with square brackets.
	# Replace any NdS(l|h)M expressions with _[N,S,(l|h),M]

	# Replace parentheses
	strarg = strarg.replace('(', '[').replace(')', ']')
	# print(strarg) #DEBUG

	# Iterate through replacing d operators
	while 'd' in strarg:
		strarg = parseexpression(strarg)
	# print(strarg) #DEBUG

	# Re-replace function name and parentheses
	strarg = strarg.replace('_', 'roll').replace('[', '(').replace(']', ')')
	# print(strarg) #DEBUG
	return strarg

# Alias for filter and then translate instructions
def interpretinstructions(strarg):
	return translateinstructions(filterinstructions(strarg))

