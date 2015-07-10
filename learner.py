#Joshua Pepperman

import sys
import cPickle as pickle

#inputFile = open("input.txt")
if len(sys.argv) > 1 and ".txt" in sys.argv[1]:
	inputFile = open(sys.argv[1])
else:
	print("Enter a .txt file to learn from.")
	exit()
#0 is the beginning of a sentence, 1 is the end.
wordDict = {0:[], 1:[]}

try:
	with open('brain', 'rb') as f:
		wordDict = pickle.load(f)
except IOError:
	#this is for when there isn't a brain file already. Should only do this once.
	pass

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

wordList = []
counter = 0
for line in inputFile:
	words = line.split()

	#for w in words:
	#	wordList.append(w)
	wordList.extend(words)
	#if len(wordList) % 1000 > counter:
	#	print("Working: " + str(len(wordList)))
	#	counter = len(wordList)

#print(len(wordList))

newSentence = True
punct = ['.', '!', '?']
for i in range(len(wordList)):
	#get the word we're looking at now.
	word = wordList[i]
	#print("Adding " + str(word))
	#if this is a new sentence, add the word as coming in new.
	if newSentence:
		#pdb.set_trace()
		addWord(0, word)
	#if there is punctuation on a word (or the last word from source), make it the end of a sentence
	#the second part of this checks if any punctuation marks are in word
	#if i == len(wordList)-1 or [j for j in punct if j in word]:
	if i == len(wordList)-1 or '.' in word or '!' in word or '?' in word:
		addWord(word, 1)
	else:
		addWord(word, wordList[i+1])

with open('brain', 'wb') as f:
	pickle.dump(wordDict, f)
