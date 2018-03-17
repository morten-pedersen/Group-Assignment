import os
import fileHandler
import math


def getInitializedTrainData():
	"""
	This function will go through the training set and return the positive and negative wordfrequency as well as the their probability.
	:return: A dictionary with the following keys as strings:
	posFreq - the frequency of words that are in positive reviews
	negFreq - the frequency of words that are in negative reviews
	posProb - the positive probability - amount of positive reviews / total number of reviews
	negProb - the negative probability - amount of negative reviews / total number of reviews
	"""
	dir_path = os.path.dirname(os.path.realpath(__file__))  # get the path to python file
	os.chdir(dir_path)
	posTrainPath = os.getcwd() + "\\Data\\train\\pos\\"  # relative path to positive train positive reviews, make sure data folder is in same directory as this py file.
	negTrainPath = os.getcwd() + "\\Data\\train\\neg\\"
	posTrainFiles = fileHandler.getfilelist(posTrainPath)  # list of files
	negTrainFiles = fileHandler.getfilelist(negTrainPath)  # list of files
	posWords = fileHandler.getwords(posTrainFiles)  # list of words
	negWords = fileHandler.getwords(negTrainFiles)  # list of words
	posFrequency = fileHandler.makeWordFrequencyDict(
		posWords)  # dictionary with frequency of words found in positive reviews
	negFrequency = fileHandler.makeWordFrequencyDict(
		negWords)  # dictionary with frequency of words found in negative reviews
	posProbability = posTrainFiles.__len__()/(posTrainFiles.__len__() + negTrainFiles.__len__())  # baseline prob
	negProbability = negTrainFiles.__len__()/(posTrainFiles.__len__() + negTrainFiles.__len__())  # .50ish?
	dir_path = os.path.dirname(os.path.realpath(__file__))  # get the path to python file
	os.chdir(dir_path)
	initializedTrainingData = {"posFreq":posFrequency, "negFreq":negFrequency,
							   "posProb":posProbability, "negProb":negProbability}
	return initializedTrainingData


def makeClassPrediction(path, wordCountDict, priorProb):
	"""
	This function will predict if the review is positive or negative, depending on what is given as arguments
	:param path: the path to the txt file
	:param wordCountDict: the positive or negative review wordcounts
	:param priorProb: the prior probability for positive or negative review, should be around 0.50
	:return: a float with 2 decimals
	"""
	countedText = fileHandler.getwords(path = path)  # get the words from the file
	countedText = fileHandler.makeWordFrequencyDict(countedText)  # make a dict with word frequency in given file
	prediction = 0  # declare prediction
	for word in countedText:  # go through every word
		if word in wordCountDict:  # skip those words we don't have seen before
			prediction += (wordCountDict[word]*(countedText[word] + 1))  # multiply word frequency
	prediction = priorProb*prediction  # multiply prior probability
	return round(math.log10(prediction), 2)  # return float with 2 decimals


def finalPrediction(posPrediction, negPrediction):
	"""
	Function decides if the prediction is positive or negative
	:param posPrediction: float number
	:param negPrediction:  float number
	:return: string
	"""
	if posPrediction > negPrediction:
		return "positive"
	else:
		return "negative"

# def finalPrediction(text):
#
# 	posPrediction = makeClassPrediction(text, posFrequency, posProbability, testDictionary)
#
# 	negPrediction = makeClassPrediction(text, negFrequency, negProbability, testDictionary)
#
# 	if negPrediction > posPrediction:
# 		return -1
# 	return 1
#
# print("For this review: {0}".format(reviews[0][0]))
# print("")
# print("The predicted label is ", make_decision(reviews[0][0]))
# print("The actual label is ", reviews[0][1])
#
#
#
