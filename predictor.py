import math

import dataHandler
import fileHandler as fh
from dataHandler import getInitializedTrainData, getIntitializedTestData


def predictTestReviews(trainingData, testData):
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
	if trainingData is None:
		trainingData = getInitializedTrainData()
		testData = getIntitializedTestData()

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
		posPrediction = makeClassPrediction(text = currentReview, posOrNegWordCountDict = posTrainingFreq,
											priorProb = 0.5)
		negPrediction = makeClassPrediction(text = currentReview, posOrNegWordCountDict = negTrainingFreq,
											priorProb = 0.5)

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
		posPrediction = makeClassPrediction(text = currentReview, posOrNegWordCountDict = posTrainingFreq,
											priorProb = 0.5)
		negPrediction = makeClassPrediction(text = currentReview, posOrNegWordCountDict = negTrainingFreq,
											priorProb = 0.5)

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


def makeClassPrediction(posOrNegWordCountDict, priorProb, path = None, text = None):
	"""
	This function will predict if the review is positive or negative, depending on what wordcount dictionary that  is given as arguments
	:param path: the path to the txt file
	:param posOrNegWordCountDict: the positive or negative review wordcounts
	:param priorProb: the prior probability for positive or negative review, should be around 0.50
	:return: a float with 2 decimals
	"""
	if path is None:
		countedText = fh.makeWordFrequencyDict(text)
	else:
		countedText = fh.getwords(path = path)  # get the words from the file
		countedText = fh.makeWordFrequencyDict(countedText)  # make a dict with word frequency in given file
	prediction = 0  # declare prediction
	for word in countedText:  # go through every word
		if word in posOrNegWordCountDict:  # skip those words we don't have seen before
			prediction += (posOrNegWordCountDict[word]*(countedText[word] + 1))  # multiply word frequency
	prediction = priorProb*prediction  # multiply prior probability
	return round(math.log10(prediction), 5)  # return float with 5 decimals TODO: this is probably wrong


def predictInput(text):
	"""
	This function will attempt to predict whether a review that is written by the user is positive or negative.
	:param text: the input from the user
	:return: a set with the results.
	"""
	trainingData = dataHandler.getInitializedTrainData()
	posFrequency = trainingData["posFreq"]
	negFrequency = trainingData["negFreq"]
	posProbability = trainingData["posProb"]
	negProbability = trainingData["negProb"]
	listOfWords = fh.getwordsfrominput(text)
	# countedWords = fh.makeWordFrequencyDict(listOfWords)
	posPrediction = makeClassPrediction(posFrequency, posProbability, text = listOfWords)
	negPrediction = makeClassPrediction(negFrequency, negProbability, text = listOfWords)
	predictedResult = finalPrediction(posPrediction, negPrediction)
	results = {"It is predicted to be: " + predictedResult, "posPrediction: " + (str(posPrediction)),
			   "negPrediction: " + (str(negPrediction))}
	return results


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
