import math

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
	This function will predict if the review is positive or negative, depending on what wordcount dictionary that  is given as arguments
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
	return round(math.log10(prediction), 5)  # return float with 5 decimals TODO: this is probably wrong


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
