import os
import time
import main
import dataHandler
import fileHandler
import predictor as predict

path = main.get_path()


def testingTwoPredictions(useStopWords = False):
	"""
	This test tests what the predictions are for a positive and negative test review
	"""
	startTime = time.time()
	if useStopWords:
		print("Running testingTwoPredictions. WITH STOPWORDS")
	else:
		print("Running testingTwoPredictions...")

	posReviewPath = path + "\\test\\pos\\1_10.txt"  # positive review
	negReviewPath = path + "\\test\\neg\\0_2.txt"  # negative review
	trainingData = dataHandler.getInitializedTrainData(useStopWords)
	posFrequency = trainingData["posFreq"]
	negFrequency = trainingData["negFreq"]
	posProbability = trainingData["posProb"]
	negProbability = trainingData["negProb"]
	print("Predicting if a positive review is positive or negative...")
	print("positive prediction is")
	posPrediction = predict.makeClassPrediction(path = posReviewPath, posOrNegWordCountDict = posFrequency,
	                                            priorProb = posProbability)
	print(posPrediction)
	print("negative prediction is")
	negPrediction = predict.makeClassPrediction(path = posReviewPath, posOrNegWordCountDict = negFrequency,
	                                            priorProb = negProbability)
	print(negPrediction)
	prediction = predict.finalPrediction(posPrediction, negPrediction)
	print("It is a " + prediction + " review")
	print("")
	print("Predicting if a negative review is positive or negative...")
	print("positive prediction is")
	posPrediction = predict.makeClassPrediction(path = negReviewPath, posOrNegWordCountDict = posFrequency,
	                                            priorProb = posProbability)
	print(posPrediction)
	print("negative prediction is")
	negPrediction = predict.makeClassPrediction(path = negReviewPath, posOrNegWordCountDict = negFrequency,
	                                            priorProb = negProbability)
	print(negPrediction)
	prediction = predict.finalPrediction(posPrediction, negPrediction)
	print("It is a " + prediction + " review")
	endTime = time.time()
	print("Test is complete.")
	print("Test took: " + str(round(endTime - startTime, 2)) + " sec")


def testingTestDataProcessing():
	"""
	This test checks that getIntitializedTestData() returns something
	"""
	startTime = time.time()
	print("Running testingTestDataProcessing...")  # running the test
	if dataHandler.getIntitializedTestData() is dict:
		print("Data was processed")
	else:
		print("Something went wrong")
	endTime = time.time()
	print("Test is complete.")
	print("Test took: " + str(round(endTime - startTime, 2)) + " sec")


def testPredictTestReviews():
	"""
	This test will try to predict all the test reviews.
	Accuracy of the test and duration of test is printed.
	"""
	startTime = time.time()
	print("Running testPredictTestReviews...")
	results = predict.predictTestReviews()
	print(results)
	numberOfReviews = 25000
	print(
		str((results["correctPredictions"] - numberOfReviews) / numberOfReviews * (100) * -1) + "% is the error rate ")
	endTime = time.time()
	print("Test is complete.")
	print("Test took: " + str(round(endTime - startTime, 2)) + " sec")


def testdataSaving():
	"""
	This test will try to save a file containing the string "test".
	"""
	testString = "test"
	print("Attempting to save: \n", testString, "\n as\n testString.test")
	fileHandler.save_object(testString, "testString.test")


def testdataLoading():
	"""
	This test will attempt to load the saved file that contains the string "test"
	"""
	print("Attempting to load from file...")
	testString = "test"
	print("Expecting from file: ", testString)
	loadedString = fileHandler.load_object("testString.test")
	if type(loadedString) is type(testString):
		print("Value loaded from file: ", loadedString)
	else:
		print("Something went wrong, the file has the wrong type, expected string but got: ", type(loadedString))


def testSavingTrainingDataToFile():
	"""
	This test will attempt to save trainingdata to a file with the name testTrainingData.test
	"""
	trainingData = dataHandler.getInitializedTrainData()
	print("Attempting to save the trainingdata to testTrainingData.test")
	fileHandler.save_object(trainingData, "testTrainingData.test")
	print("Something was saved.")


def testLoadTrainingDataFromfile():
	"""
	This test will attempt to load the saved file testTrainingData.test that should contain a dictionary, and checks that it does contain a dict
	"""
	print("Attempting to load training data from file...")
	trainingData = fileHandler.load_object("testTrainingData.test")
	if type(trainingData) is not None:
		print("A dictionary was loaded as expected.")
	else:
		print("Something went wrong, the file has the wrong type, expected a dict but got: ", type(trainingData))


def cleanupFilesFromTests():
	"""
	This function will remove files that were created during the tests.
	"""
	dir_path = os.path.dirname(os.path.realpath(__file__))  # get the path to python file
	os.chdir(dir_path)  # TODO try except stuff here and test it
	try:
		os.remove(os.getcwd() + "\\testString.test")
		print("testString.test was removed.")
	except Exception as e:
		pass

	try:
		os.remove(os.getcwd() + "\\testdata.test")
		print("testdata.test was removed.")
	except Exception as e:
		pass

	try:
		os.remove(os.getcwd() + "\\trainingdata.test")
		print("trainingdata.test was removed.")
	except Exception as e:
		pass

	try:
		os.remove(os.getcwd() + "\\testTrainingData.test")
		print("testTrainingData.test was removed.")
	except Exception as e:
		pass

	print("Test files has been removed.")


def savingAndLoadingTests():
	"""
	The function for testing loading and saving data. It executes the following tests.
	"""
	startTime = time.time()
	testdataSaving()  # testString.txt
	endTime = time.time()
	print("testdataSaving took: " + str(round(endTime - startTime, 2)) + " sec\n")
	testdataLoading()
	endTime = time.time()
	print("testdataLoading took: " + str(round(endTime - startTime, 2)) + " sec\n")
	testSavingTrainingDataToFile()  # testTrainingData.test
	endTime = time.time()
	print("testSavingTrainingDataToFile took: " + str(round(endTime - startTime, 2)) + " sec\n")
	testLoadTrainingDataFromfile()
	endTime = time.time()
	print("testLoadTrainingDataFromfile took: " + str(round(endTime - startTime, 2)) + " sec\n")
	endTime = time.time()
	print("Test is complete.")
	print("Test took: " + str(round(endTime - startTime, 2)) + " sec")
	print("Running cleanup...")
	cleanupFilesFromTests()


def createTrainingdataFiles(useStopWords = False):
	"""
	This function will process trainingdata and save the processed data to a file by the name trainingdata.test
	"""
	print("Creating preprocessed trainingData. Using stopwords? ", useStopWords)
	if useStopWords:
		trainingdata = dataHandler.getInitializedTrainData(useStopWords)
	else:
		trainingdata = dataHandler.getInitializedTrainData()
	fileHandler.save_object(trainingdata, "trainingdata.test")
	print("Created trainingdata.test...")
	print("Data has been processed and written to trainingdata.test.")


def createTestdataFiles():
	"""
	This function will process the testdata and save the processed data to a file by the name testdata.test
	"""
	print("Creating preprocessed testData...")
	testdata = dataHandler.getIntitializedTestData()
	fileHandler.save_object(testdata, "testdata.test")
	print("Created testdata.test...")
	print("Data has been processed and written to testdata.test.")


def testPredictionWithLoadedFile():
	"""
	This test will attempt to predict the testdata, using the preprocessed data
	Throws FileNotFoundError if the preprocessed data cant be found
	:return:
	"""
	print("Running testPredictionWithLoadedFile...")
	startTime = time.time()
	try:
		trainingdata = fileHandler.load_object("trainingdata.test")
		testdata = fileHandler.load_object("testdata.test")
		results = predict.predictTestReviews(trainingdata, testdata)
		print(results)
		numberOfReviews = 25000
		print(str(
			(results["correctPredictions"] - numberOfReviews) / numberOfReviews * (100) * -1) + "% is the error rate ")
		endTime = time.time()
		print("Test is complete.")
		print("Test took: " + str(round(endTime - startTime, 2)) + " sec")
	except FileNotFoundError as e:
		print("Exception occoured, please create the test files first then run this again: ", e)


def testStopWords():
	"""
	First run regular prediction on test set, then do one using stopwords
	"""
	startTime = time.time()
	testingTwoPredictions()  # WITHOUT STOPWORDS
	testingTwoPredictions(useStopWords = True)
	endTime = time.time()
	print("Both tests are complete.")
	print("Tests took: " + str(round(endTime - startTime, 2)) + " sec in total")


def bigStopWordTest():
	"""
	This test will first process the training and test data, then try to do predictions.
	The training set will be using stopwords
	"""
	startTime = time.time()
	try:
		trainingdata = fileHandler.load_object("trainingdata.test")
		testdata = fileHandler.load_object("testdata.test")
		results = predict.predictTestReviews(trainingdata, testdata)
		print(results)
		numberOfReviews = 25000
		print(str(
			(results["correctPredictions"] - numberOfReviews) / numberOfReviews * (100) * -1) + "% is the error rate ")
		endTime = time.time()
		print("Test is complete.")
		print("Test took: " + str(round(endTime - startTime, 2)) + " sec")
	except FileNotFoundError as e:
		print("Exception occoured: ", e)
		print("Attempting to process data and then trying again.")
		createTrainingdataFiles(useStopWords = True)
		createTestdataFiles()
		bigStopWordTest()
