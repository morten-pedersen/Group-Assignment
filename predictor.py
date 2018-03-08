import naiveBayes
import re

def openTestText ():
	listOfTestWords = [] # Opens a single textfile with path
	with open("C:\\Users\\morte\\PycharmProjects\\Group-Assignment\\Data\\test\\pos\\25_10.txt", encoding = "utf8") as file:
		testText = file.read().lower()
		file.close()
		testText = re.sub('[\'()/!.":,!?]', '', testText)
		testText = re.sub('[<>]', ' ', testText)
		testWords = list(testText.split())
		for testWord in testWords:
			if testWord.__len__() > 1 and testWord not in "br":
				listOfTestWords.append(testWord)
	return listOfTestWords()

def testTextFrequency(listOfTestWords):
	testDictionary = {}
	for testWord in openTestText():
		if testWord in testDictionary:
			testDictionary[testWord] += 1
		else:
			testDictionary[testWord] = 1
	return testDictionary



