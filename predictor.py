import math
import os

import fileHandler as fh


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
	posTrainFiles = fh.getfilelist(posTrainPath)  # list of files
	negTrainFiles = fh.getfilelist(negTrainPath)  # list of files
	posWords = fh.getwords(posTrainFiles)  # list of words
	negWords = fh.getwords(negTrainFiles)  # list of words
	posFrequency = fh.makeWordFrequencyDict(
		posWords)  # dictionary with frequency of words found in positive reviews
	negFrequency = fh.makeWordFrequencyDict(
		negWords)  # dictionary with frequency of words found in negative reviews
	posProbability = posTrainFiles.__len__()/(posTrainFiles.__len__() + negTrainFiles.__len__())  # baseline prob
	negProbability = negTrainFiles.__len__()/(posTrainFiles.__len__() + negTrainFiles.__len__())  # .50ish?
	dir_path = os.path.dirname(os.path.realpath(__file__))  # get the path to python file
	os.chdir(dir_path)
	initializedTrainingData = {"posFreq":posFrequency, "negFreq":negFrequency,
							   "posProb":posProbability, "negProb":negProbability}
	return initializedTrainingData


def getIntitializedTestData():
	"""
	Test data is gathered, processed and put in dictionaries
	:return: dict with positive and negative reviews
	Keys:
	posReviews - the positive reviews
	negReviews - the negative reviews
	"""
	dir_path = os.path.dirname(os.path.realpath(__file__))  # get the path to python file
	os.chdir(dir_path)
	posTrainPath = os.getcwd() + "\\Data\\test\\pos\\"  # relative path to positive train positive reviews, make sure data folder is in same directory as this py file.
	negTrainPath = os.getcwd() + "\\Data\\test\\neg\\"
	posTrainFiles = fh.getfilelist(posTrainPath)  # list of files
	negTrainFiles = fh.getfilelist(negTrainPath)  # list of files
	i = 0
	posReviews = {}
	negReviews = {}
	while posTrainFiles.__len__() is not 0:  # while list is not empty get reviews and put them into a dict
		review = fh.getwords(path = posTrainFiles.pop())
		posReviews[i] = review  # key is just a number, use __len__() on the dict to find number of reviews later
		i += 1
	i = 0
	while negTrainFiles.__len__() is not 0:
		review = fh.getwords(path = negTrainFiles.pop())
		negReviews[i] = review
		i += 1

	initializedTestData = {"posReviews":posReviews, "negReviews":negReviews}
	return initializedTestData


def predictTestReviews(trainingData = getInitializedTrainData(), testData = getIntitializedTestData()):
	"""
	This function will go through all set of test reviews and attempt to predict if it is positive or negative and save the results
	:param trainingData: dict that looks like this {"posFreq":posFrequency, "negFreq":negFrequency,
							  					    "posProb":posProbability, "negProb":negProbability}
	:param testData: dict that looks like this {"posReviews":posReviews, "negReviews":negReviews}
	:return: a dictionary containing the results, key strings are:
	predictedPositive
	predictedNegative
	correctPredictions
	incorrectPredictions
	they contain integers
	"""
	predictedPositive = 0
	predictedNegative = 0
	correctPredictions = 0
	incorrectPredictions = 0
	posTrainingFreq = trainingData["posFreq"]
	negTrainingFreq = trainingData["negFreq"]
	posTestReviews = testData["posReviews"]
	negTestReviews = testData["negReviews"]
	counter = 0
	while posTestReviews.__len__() > counter:
		currentReview = posTestReviews[counter]
		posPrediction = makeClassPrediction(text = currentReview, wordCountDict = posTrainingFreq, priorProb = 0.5)
		negPrediction = makeClassPrediction(text = currentReview, wordCountDict = negTrainingFreq, priorProb = 0.5)

		if finalPrediction(posPrediction, negPrediction) is "positive":
			correctPredictions += 1
			predictedPositive += 1
		else:
			incorrectPredictions += 1
			predictedNegative += 1
		counter += 1
	counter = 0
	while negTestReviews.__len__() > counter:
		currentReview = negTestReviews[counter]
		posPrediction = makeClassPrediction(text = currentReview, wordCountDict = posTrainingFreq, priorProb = 0.5)
		negPrediction = makeClassPrediction(text = currentReview, wordCountDict = negTrainingFreq, priorProb = 0.5)

		if finalPrediction(posPrediction, negPrediction) is "negative":
			correctPredictions += 1
			predictedNegative += 1
		else:
			incorrectPredictions += 1
			predictedPositive += 1
		counter += 1
	results = {}
	results["predictedPositive"] = predictedPositive
	results["predictedNegative"] = predictedNegative
	results["correctPredictions"] = correctPredictions
	results["incorrectPredictions"] = incorrectPredictions
	return results


# TODO priorprob = log(0.5)????


def makeClassPrediction(wordCountDict, priorProb, path = None, text = None):
	"""
	This function will predict if the review is positive or negative, depending on what is given as arguments
	:param path: the path to the txt file
	:param wordCountDict: the positive or negative review wordcounts
	:param priorProb: the prior probability for positive or negative review, should be around 0.50
	:return: a float with 2 decimals
	"""
	if path is None:  # hack - TODO fix this later
		countedText = text
		countedText = fh.makeWordFrequencyDict(countedText)
	if path is not None:  # hack - TODO fix this later
		countedText = fh.getwords(path = path)  # get the words from the file
		countedText = fh.makeWordFrequencyDict(countedText)  # make a dict with word frequency in given file
	prediction = 0  # declare prediction
	for word in countedText:  # go through every word
		if word in wordCountDict:  # skip those words we don't have seen before
			prediction += (wordCountDict[word]*(countedText[word] + 1))  # multiply word frequency
	prediction = priorProb*prediction  # multiply prior probability
	return round(math.log10(prediction), 5)  # return float with 5 decimals


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
