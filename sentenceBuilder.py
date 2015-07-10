#Joshua Pepperman

import pdb
import pprint
import random
import cPickle as pickle

with open('brain', 'rb') as f:
	wordDict = pickle.load(f)

#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(wordDict)

def writeSentence():
	sentence = []
	firstWordChoices = []
	for wordAndCount in wordDict[0]:
		for i in range(wordAndCount[1]):
			firstWordChoices.append(wordAndCount[0])
	firstWord = random.choice(firstWordChoices)
	sentence.append(firstWord)

	nextWordChoices = []
	for wordAndCount in wordDict[firstWord]:
		for i in range(wordAndCount[1]):
			nextWordChoices.append(wordAndCount[0])
	nextWord = random.choice(nextWordChoices)

	while nextWord != 1:
		sentence.append(nextWord)
		nextWordChoices = []
		for wordAndCount in wordDict[nextWord]:
			for i in range(wordAndCount[1]):
				nextWordChoices.append(wordAndCount[0])
		nextWord = random.choice(nextWordChoices)
	
	toPrint = ""
	for word in sentence:
		toPrint = toPrint + word + " "

	print(toPrint)

writeSentence()
