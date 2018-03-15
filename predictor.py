import naiveBayes
import re
import os


def openTestText():
	listOfTestWords = []  # Opens a single textfile with path
	path = os.getcwd() + "\\Data\\test\\pos\\25_10.txt"
	with open(path, encoding = "utf8") as file:
		testText = file.read().lower()
		file.close()
		testText = re.sub('[\'()/!.":,!?]', '', testText)
		testText = re.sub('[<>]', ' ', testText)
		testWords = list(testText.split())
		for testWord in testWords:
			if testWord.__len__() > 1 and testWord not in "br":
				listOfTestWords.append(testWord)
	return listOfTestWords


def testTextFrequency(listOfTestWords):
	testDictionary = {}
	for testWord in openTestText():
		if testWord in testDictionary:
			testDictionary[testWord] += 1
		else:
			testDictionary[testWord] = 1
	return testDictionary


def makeClassPrediction(text, H_wordCountDict, H_probability, H_Count):
	"""
	H is a negative or positive review
	:param text: the text of the review
	:param H_wordCountDict: the dictionary containing the counted words in the type of review
	:param H_probability: The probability of it being negative or positive? So by 0.5 if the set of review is divided in equal parts?
	:param H_Count: ????? what is this ?????
	:return: probability from 0 - 1???
	"""



def finalPrediction(text):

	posPrediction = makeClassPrediction(text, posFrequency, posProbability, testDictionary)

	negPrediction = makeClassPrediction(text, negFrequency, negProbability, testDictionary)

	if negPrediction > posPrediction:
		return -1
	return 1


