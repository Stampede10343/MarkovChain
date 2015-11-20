import random

class MarkovKey:
	def __init__(self, text):
		self.text = text
		self.occurences = 1

	def addOccurence(self):
		self.occurences += 1

class MarkovValueList:
	def __init__(self, value):
		self.values = {value: 1}

	def addValue(self, value):
		if value in self.values:
			self.values[value] = self.values[value] += 1
		else:
			self.values[value] = {value: 1}

class Input:
	def __init__(self, input, chainLength, generate):
		self.input = input
		self.length = chainLength
		self.markovMap = {}
		self.wordsToPrint = generate

	def MakeChains(self):
		file = open(self.input, 'r')
		splitInput = file.read().split()
		i = 0
		while i < len(splitInput) - self.length:
			key = ""
			for a in range(i, i + self.length):
				key += splitInput[a] + ' '

			if key in self.markovMap:
				self.markovMap[key].append(splitInput[i+self.length])
			else:
				self.markovMap[key] = [splitInput[i+self.length]]
			i+=1

	def Output(self):
		for i in range(0, self.wordsToPrint/self.length):
			key = random.choice(self.markovMap.keys())
			value = random.choice(self.markovMap[key])
			print key.strip() + ' ', self.markovMap[key][self.markovMap[key].index(value)].strip() + ' ',



input = Input("text.txt", 3, 18)

input.MakeChains()
input.Output()
#print input.markovMap.keys()
#print input.markovMap