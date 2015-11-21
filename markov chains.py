import random

class MarkovValue:
	def __init__(self, value):
		self.values = {value: 1}

	def addValue(self, value):
		if value in self.values:
			occurences = self.values[value]
			occurences += 1
			self.values[value] = occurences
		else:
			self.values[value] = 1

	def getBest(self):
		bestValue = 0
		v = ""

		for value in self.values.keys():
			if self.values[value] > bestValue:
				bestValue = self.values[value]
				v = value

		return v

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
				curValue = self.markovMap[key]
				curValue.addValue(splitInput[i+self.length])
				self.markovMap[key] = curValue

			else:
				self.markovMap[key] = MarkovValue(splitInput[i+self.length])

			i+=1

	def Output(self):
		for i in range(0, self.wordsToPrint/self.length):
			key = random.choice(self.markovMap.keys())
			value = self.markovMap[key].getBest()
			print key.strip() + ' ', value + ' ',



input = Input("text.txt", 3, 24)

input.MakeChains()
input.Output()
#print input.markovMap.keys()
#print input.markovMap