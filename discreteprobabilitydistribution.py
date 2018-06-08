class Distribution:
	def __init__(self, *positionalparameters):
		if len(positionalparameters) != 0:
			distribution = positionalparameters[0]
		else:
			distribution = {}
		self.distribution = distribution

	def populateIndividualChoice(self, choicevalue, count=1):
		if choicevalue not in self.distribution:
			self.distribution[choicevalue] = count
		else:
			self.distribution[choicevalue] += count

	def normalize(self, scale=1):
		total = sum([self.distribution[x] for x in self.distribution])
		newdistribution=Distribution()
		for choice in self.distribution:
			newdistribution.distribution[choice]=scale*self.distribution[choice]/total
		return newdistribution

	# Normalize in-place
	def inormalize(self, scale=1):
		total = sum([self.distribution[x] for x in self.distribution])
		for choice in self.distribution:
			self.distribution[choice]=scale*self.distribution[choice]/total

	def filledDistribution(self):
		filleddistribution = {}
		for x in range(min(self.distribution), max(self.distribution) + 1):
			if not isinstance(x, int):
				raise TypeError("Unsupported data type " + type(x))
			if x in self.distribution:
				filleddistribution[x] = self.distribution[x]
			else:
				filleddistribution[x] = 0
		return filleddistribution

	def plotformat(self):
		plotformatteddistribution = []
		filleddistribution = self.filledDistribution()
		plotformatteddistribution.append(sorted(list(filleddistribution.keys())))
		plotformatteddistribution.append([filleddistribution[x] for x in plotformatteddistribution[0]])
		return plotformatteddistribution



	# Simple 1-argument Operators

	def __neg__(self):
		return self.neg()
		
	def neg(self):
		newdistribution = {}
		for x in a:
			newdistribution[-x] = self.distribution[x]
		return Distribution(newdistribution)

	def __pos__(self):
		return self.pos()
		
	def pos(self):
		newdistribution = {}
		for x in a:
			newdistribution[+x] = self.distribution[x]
		return Distribution(newdistribution)

	def __abs__(self):
		return self.abs()
		
	def abs(self):
		newdistribution = {}
		for x in a:
			newindex=abs(x)
			if newindex not in newdistribution:
				newdistribution[newindex] = 0
			newdistribution[newindex] = newdistribution[newindex] + self.distribution[x]
		return Distribution(newdistribution)


	# Simple 2-argument Operators and Reverse 2-argument Operators

	def __add__(self, something):
		if isinstance(something, self.__class__):
			return self.add(self.distribution, something.distribution)
		elif isinstance(something, (int, float)):
			return self.add(self.distribution, {something: 1})
		else:
			raise TypeError("Unsupported operand type for: ", self.__class__, type(something))
	def __radd__(self, something):
		if isinstance(something, self.__class__):
			return self.add(something.distribution, self.distribution)
		elif isinstance(something, (int, float)):
			return self.add({something: 1}, self.distribution)
		else:
			raise TypeError("Unsupported operand type for: ", self.__class__, type(something))

	def add(self, a, b):
		newdistribution = {}
		for x in a:
			for y in b:
				newindex = x + y
				if newindex not in newdistribution:
					newdistribution[newindex] = 0
				newdistribution[newindex] = newdistribution[newindex] + a[x] + b[y] - 1
		return Distribution(newdistribution)

	def __sub__(self, something):
		if isinstance(something, self.__class__):
			return self.sub(self.distribution, something.distribution)
		elif isinstance(something, (int, float)):
			return self.sub(self.distribution, {something: 1})
		else:
			raise TypeError("Unsupported operand type for: ", self.__class__, type(something))
	def __rsub__(self, something):
		if isinstance(something, self.__class__):
			return self.sub(something.distribution, self.distribution)
		elif isinstance(something, (int, float)):
			return self.sub({something: 1}, self.distribution)
		else:
			raise TypeError("Unsupported operand type for: ", self.__class__, type(something))

	def sub(self, a, b):
		newdistribution = {}
		for x in a:
			for y in b:
				newindex = x - y
				if newindex not in newdistribution:
					newdistribution[newindex] = 0
				newdistribution[newindex] = newdistribution[newindex] + a[x] + b[y] - 1
		return Distribution(newdistribution)

	def __mul__(self, something):
		if isinstance(something, self.__class__):
			return self.mul(self.distribution, something.distribution)
		elif isinstance(something, (int, float)):
			return self.mul(self.distribution, {something: 1})
		else:
			raise TypeError("Unsupported operand type for: ", self.__class__, type(something))
	def __rmul__(self, something):
		if isinstance(something, self.__class__):
			return self.mul(something.distribution, self.distribution)
		elif isinstance(something, (int, float)):
			return self.mul({something: 1}, self.distribution)
		else:
			raise TypeError("Unsupported operand type for: ", self.__class__, type(something))

	def mul(self, a, b):
		newdistribution = {}
		for x in a:
			for y in b:
				newindex = x * y
				if newindex not in newdistribution:
					newdistribution[newindex] = 0
				newdistribution[newindex] = newdistribution[newindex] + a[x] + b[y] - 1
		return Distribution(newdistribution)

	def __truediv__(self, something):
		if isinstance(something, self.__class__):
			return self.truediv(self.distribution, something.distribution)
		elif isinstance(something, (int, float)):
			return self.truediv(self.distribution, {something: 1})
		else:
			raise TypeError("Unsupported operand type for: ", self.__class__, type(something))
	def __rtruediv__(self, something):
		if isinstance(something, self.__class__):
			return self.truediv(something.distribution, self.distribution)
		elif isinstance(something, (int, float)):
			return self.truediv({something: 1}, self.distribution)
		else:
			raise TypeError("Unsupported operand type for: ", self.__class__, type(something))

	def truediv(self, a, b):
		newdistribution = {}
		for x in a:
			for y in b:
				newindex = x / y
				if newindex not in newdistribution:
					newdistribution[newindex] = 0
				newdistribution[newindex] = newdistribution[newindex] + a[x] + b[y] - 1
		return Distribution(newdistribution)

	def __floordiv__(self, something):
		if isinstance(something, self.__class__):
			return self.floordiv(self.distribution, something.distribution)
		elif isinstance(something, (int, float)):
			return self.floordiv(self.distribution, {something: 1})
		else:
			raise TypeError("Unsupported operand type for: ", self.__class__, type(something))
	def __rfloordiv__(self, something):
		if isinstance(something, self.__class__):
			return self.floordiv(something.distribution, self.distribution)
		elif isinstance(something, (int, float)):
			return self.floordiv({something: 1}, self.distribution)
		else:
			raise TypeError("Unsupported operand type for: ", self.__class__, type(something))

	def floordiv(self, a, b):
		newdistribution = {}
		for x in a:
			for y in b:
				newindex = x // y
				if newindex not in newdistribution:
					newdistribution[newindex] = 0
				newdistribution[newindex] = newdistribution[newindex] + a[x] + b[y] - 1
		return Distribution(newdistribution)

	def __mod__(self, something):
		if isinstance(something, self.__class__):
			return self.mod(self.distribution, something.distribution)
		elif isinstance(something, (int, float)):
			return self.mod(self.distribution, {something: 1})
		else:
			raise TypeError("Unsupported operand type for: ", self.__class__, type(something))
	def __rmod__(self, something):
		if isinstance(something, self.__class__):
			return self.mod(something.distribution, self.distribution)
		elif isinstance(something, (int, float)):
			return self.mod({something: 1}, self.distribution)
		else:
			raise TypeError("Unsupported operand type for: ", self.__class__, type(something))

	def mod(self, a, b):
		newdistribution = {}
		for x in a:
			for y in b:
				newindex = x % y
				if newindex not in newdistribution:
					newdistribution[newindex] = 0
				newdistribution[newindex] = newdistribution[newindex] + a[x] + b[y] - 1
		return Distribution(newdistribution)

	def __pow__(self, something):
		if isinstance(something, self.__class__):
			return self.pow(self.distribution, something.distribution)
		elif isinstance(something, (int, float)):
			return self.pow(self.distribution, {something: 1})
		else:
			raise TypeError("Unsupported operand type for: ", self.__class__, type(something))
	def __rpow__(self, something):
		if isinstance(something, self.__class__):
			return self.pow(something.distribution, self.distribution)
		elif isinstance(something, (int, float)):
			return self.pow({something: 1}, self.distribution)
		else:
			raise TypeError("Unsupported operand type for: ", self.__class__, type(something))

	def pow(self, a, b):
		newdistribution = {}
		for x in a:
			for y in b:
				newindex = x ** y
				if newindex not in newdistribution:
					newdistribution[newindex] = 0
				newdistribution[newindex] = newdistribution[newindex] + a[x] + b[y] - 1
		return Distribution(newdistribution)
