import os
import time

import predictor as predict


def testingPredictions():
	"""
	This function allow us to test quickly what the predictions are
	"""
	dir_path = os.path.dirname(os.path.realpath(__file__))  # get the path to python file
	os.chdir(dir_path)
	posReviewPath = os.getcwd() + "\\Data\\test\\pos\\1_10.txt"  # positive review
	negReviewPath = os.getcwd() + "\\Data\\test\\neg\\0_2.txt"  # negative review
	trainingData = predict.getInitializedTrainData()
	posFrequency = trainingData["posFreq"]
	negFrequency = trainingData["negFreq"]
	posProbability = trainingData["posProb"]
	negProbability = trainingData["negProb"]
	print("Predicting if a positive review is positive or negative...")
	print("positive prediction is")
	posPrediction = predict.makeClassPrediction(path = posReviewPath, wordCountDict = posFrequency, priorProb = posProbability)
	print(posPrediction)
	print("negative prediction is")
	negPrediction = predict.makeClassPrediction(path =posReviewPath, wordCountDict =negFrequency, priorProb =negProbability)
	print(negPrediction)
	prediction = predict.finalPrediction(posPrediction, negPrediction)
	print("It is a " + prediction + " review")
	print("")
	print("Predicting if a negative review is positive or negative...")
	print("positive prediction is")
	posPrediction = predict.makeClassPrediction(path =negReviewPath, wordCountDict =posFrequency, priorProb =posProbability)
	print(posPrediction)
	print("negative prediction is")
	negPrediction = predict.makeClassPrediction(path =negReviewPath, wordCountDict =negFrequency, priorProb =negProbability)
	print(negPrediction)
	prediction = predict.finalPrediction(posPrediction, negPrediction)
	print("It is a " + prediction + " review")


def testingTestDataProcessing():
	trainingData = predict.getIntitializedTestData()
	return trainingData


def testPredicTestReviews():
	return predict.predictTestReviews()


startTime = time.time()
print("Running testPredicTestReviews...")
results = testPredicTestReviews()  # running the test
print(results)
numberOfReview = 25000
print(str((results["correctPredictions"]- numberOfReview)/numberOfReview*(100)*-1) + "% is the error rate ")
endTime = time.time()
print("Test is complete.")
print("Test took: " + str(round(endTime - startTime, 2)) + " sec")
print()
startTime = time.time()
print("Running testingTestDataProcessing...")
trainingData = testingTestDataProcessing()  # running the test
print("Data was processed")
endTime = time.time()
print("Test is complete.")
print("Test took: " + str(round(endTime - startTime, 2)) + " sec")
print()
startTime = time.time()
print("Running testingPredictions...")
testingPredictions()  # running the test
endTime = time.time()
print("Test is complete.")
print("Test took: " + str(round(endTime - startTime, 2)) + " sec")
