import os
import predictor as predict


def testingPredictions():
	"""
	This function allow us to test quickly what the predictions are
	"""
	posReviewPath = os.getcwd() + "\\Data\\test\\pos\\1_10.txt"  # positive review
	negReviewPath = os.getcwd() + "\\Data\\test\\neg\\0_2.txt"  # negative review
	trainingData = predict.getInitializedTrainData()
	posFrequency = trainingData["posFreq"]
	negFrequency = trainingData["negFreq"]
	posProbability = trainingData["posProb"]
	negProbability = trainingData["negProb"]
	print("Predicting if a positive review is positive or negative...")
	print("positive prediction is")
	posPrediction = predict.makeClassPrediction(posReviewPath, posFrequency, posProbability)
	print(posPrediction)
	print("negative prediction is")
	negPrediction = predict.makeClassPrediction(posReviewPath, negFrequency, negProbability)
	print(negPrediction)
	prediction = predict.finalPrediction(posPrediction, negPrediction)
	print("It is a " + prediction + " review")
	print("")
	print("Predicting if a negative review is positive or negative...")
	print("positive prediction is")
	posPrediction = predict.makeClassPrediction(negReviewPath, posFrequency, posProbability)
	print(posPrediction)
	print("negative prediction is")
	negPrediction = predict.makeClassPrediction(negReviewPath, negFrequency, negProbability)
	print(negPrediction)
	prediction = predict.finalPrediction(posPrediction, negPrediction)
	print("It is a " + prediction + " review")

testingPredictions()  # running the test