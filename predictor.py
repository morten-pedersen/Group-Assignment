import naiveBayes
import re
import os
import fileExplorer


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


def makeClassPrediction(text, wordCountDict, priorProbability, wordCountInReview):
	"""
	H is a negative or positive review
	:param text: the text of the review
	:param wordCountDict: the dictionary containing the counted words in the type of review
	:param priorProbability: The probability of it being negative or positive? So by 0.5 if the set of review is divided in equal parts?
	:param wordCountInReview: ????? what is this ?????
	:return: probability from 0 - 1???
	"""
	path = "her mangler vi path"
	countedText = fileExplorer.getwords(path = path)
	countedText = fileExplorer.makeWordFrequencyList(countedText)
	for word in countedText:
		prediction*=


def finalPrediction(text):

	posPrediction = makeClassPrediction(text, posFrequency, posProbability, testDictionary)

	negPrediction = makeClassPrediction(text, negFrequency, negProbability, testDictionary)

	if negPrediction > posPrediction:
		return -1
	return 1

print("For this review: {0}".format(reviews[0][0]))
print("")
print("The predicted label is ", make_decision(reviews[0][0]))
print("The actual label is ", reviews[0][1])



