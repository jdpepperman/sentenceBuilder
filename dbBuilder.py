#Joshua Pepperman

import pdb
import pprint
import random

#inputFile = open("input.txt")
inputFile = open("theHungerGames.txt")
#0 is the beginning of a sentence, 1 is the end.
wordDict = {0:[]}

def addWord(word, nextWord):
	#print(word, nextWord)
	added = False
	if word in wordDict:
		#print("Word in wordDict.")
		for nextWordList in wordDict[word]:
			#print(str(word) + " : " + str(nextWordList))
			if nextWord == nextWordList[0]:
				nextWordList[1] = nextWordList[1] + 1
				added = True
		if not added:
			wordDict[word].append([nextWord, 1])

	else:
		wordDict[word] = []
		wordDict[word].append([nextWord, 1])
		#print(wordDict[word])

for line in inputFile:
	line = line.rstrip()
	if line == '':
		continue
	lineList = []
	while ' ' in line:
		lineList.append(line[:line.index(' ')])
		line = line[line.index(' ')+1:]
	lineList.append(line)

	for i in range(len(lineList)):
		word = lineList[i]
		#print("Word: " + word + "\nPos: " + str(i) + " of " + str(len(lineList)))
		if lineList.index(word) == 0:
			addWord(0, word)
		#if lineList.index(word) == len(lineList)-1:
		if i == len(lineList)-1:
			addWord(word, 1)
		else:
			addWord(word, lineList[i+1])

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
