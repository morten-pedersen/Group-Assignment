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
