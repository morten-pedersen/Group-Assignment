import os
import time
import main
import data_handler
import file_handler
import predictor as predict


def testing_two_predictions(use_stop_words = False):
	"""
	This test tests what the predictions are for a positive and negative test review
	"""
	start_time = time.time()
	if use_stop_words:
		print("Running testing_two_predictions. WITH STOPWORDS")
	else:
		print("Running testing_two_predictions...")

	pos_review_path = main.get_path() + "\\test\\pos\\1_10.txt"  # positive review
	neg_review_path = main.get_path() + "\\test\\neg\\0_2.txt"  # negative review
	training_data = data_handler.get_initialized_train_data(use_stop_words)
	pos_frequency = training_data["pos_freq"]
	neg_frequency = training_data["neg_freq"]
	pos_probability = training_data["pos_prob"]
	neg_probability = training_data["neg_prob"]
	print("Predicting if a positive review is positive or negative...")
	print("positive prediction is")
	pos_prediction = predict.make_class_prediction(path = pos_review_path, pos_or_neg_word_count_dict = pos_frequency,
	                                               prior_prob = pos_probability)
	print(pos_prediction)
	print("negative prediction is")
	neg_prediction = predict.make_class_prediction(path = pos_review_path, pos_or_neg_word_count_dict = neg_frequency,
	                                               prior_prob = neg_probability)
	print(neg_prediction)
	prediction = predict.final_prediction(pos_prediction, neg_prediction)
	print("It is a " + prediction + " review")
	print("")
	print("Predicting if a negative review is positive or negative...")
	print("positive prediction is")
	pos_prediction = predict.make_class_prediction(path = neg_review_path, pos_or_neg_word_count_dict = pos_frequency,
	                                               prior_prob = pos_probability)
	print(pos_prediction)
	print("negative prediction is")
	neg_prediction = predict.make_class_prediction(path = neg_review_path, pos_or_neg_word_count_dict = neg_frequency,
	                                               prior_prob = neg_probability)
	print(neg_prediction)
	prediction = predict.final_prediction(pos_prediction, neg_prediction)
	print("It is a " + prediction + " review")
	end_time = time.time()
	print("Test is complete.")
	print("Test took: " + str(round(end_time - start_time, 2)) + " sec")


def test_predict_test_reviews():
	"""
	This test will try to predict all the test reviews.
	Accuracy of the test and duration of test is printed.
	"""
	start_time = time.time()
	print("Running test_predict_test_reviews...")
	results = predict.predict_test_reviews()
	print(results)
	number_of_reviews = 25000
	print(
		str((results["correct_predictions"] - number_of_reviews) / number_of_reviews * (
			100) * -1) + "% is the error rate ")
	end_time = time.time()
	print("Test is complete.")
	print("Test took: " + str(round(end_time - start_time, 2)) + " sec")


def testdata_saving():
	"""
	This test will try to save a file containing the string "test".
	"""
	test_string = "test"
	print("Attempting to save: \n", test_string, "\n as\n test_string.test")
	file_handler.save_object(test_string, "test_string.test")


def testdata_loading():
	"""
	This test will attempt to load the saved file that contains the string "test"
	"""
	print("Attempting to load from file...")
	test_string = "test"
	print("Expecting from file: ", test_string)
	loaded_string = file_handler.load_object("test_string.test")
	if type(loaded_string) is type(test_string):
		print("Value loaded from file: ", loaded_string)
	else:
		print("Something went wrong, the file has the wrong type, expected string but got: ", type(loaded_string))


def test_saving_training_data_to_file():
	"""
	This test will attempt to save trainingdata to a file with the name training_data.test
	"""
	training_data = data_handler.get_initialized_train_data()
	print("Attempting to save the trainingdata to training_data.test")
	file_handler.save_object(training_data, "training_data.test")
	print("Something was saved.")


def test_load_training_data_fromfile():
	"""
	This test will attempt to load the saved file training_data.test that should contain a dictionary, and checks that it does contain a dict
	"""
	print("Attempting to load training data from file...")
	training_data = file_handler.load_object("training_data.test")
	if type(training_data) is not None:
		print("A dictionary was loaded as expected.")
	else:
		print("Something went wrong, the file has the wrong type, expected a dict but got: ", type(training_data))


def cleanup_files_from_tests():
	"""
	This function will remove files that were created during the tests.
	"""
	dir_path = os.path.dirname(os.path.realpath(__file__))  # get the path to python file
	os.chdir(dir_path)  # TODO try except stuff here and test it
	try:
		os.remove(os.getcwd() + "\\test_string.test")
		print("test_string.test was removed.")
	except Exception as e:
		pass

	try:
		os.remove(os.getcwd() + "\\test_data.test")
		print("test_data.test was removed.")
	except Exception as e:
		pass

	try:
		os.remove(os.getcwd() + "\\training_data.test")
		print("training_data.test was removed.")
	except Exception as e:
		pass

	print("Test files has been removed.")


def saving_and_loading_tests():
	"""
	The function for testing loading and saving data. It executes the following tests.
	"""
	start_time = time.time()
	testdata_saving()  # testString.txt
	end_time = time.time()
	print("testdata_saving took: " + str(round(end_time - start_time, 2)) + " sec\n")
	testdata_loading()
	end_time = time.time()
	print("testdata_loading took: " + str(round(end_time - start_time, 2)) + " sec\n")
	test_saving_training_data_to_file()  # training_data.test
	end_time = time.time()
	print("test_saving_training_data_to_file took: " + str(round(end_time - start_time, 2)) + " sec\n")
	test_load_training_data_fromfile()
	end_time = time.time()
	print("test_load_training_data_fromfile took: " + str(round(end_time - start_time, 2)) + " sec\n")
	end_time = time.time()
	print("Test is complete.")
	print("Test took: " + str(round(end_time - start_time, 2)) + " sec")
	print("Running cleanup...")
	cleanup_files_from_tests()


def create_trainingdata_files(use_stop_words = False):
	"""
	This function will process trainingdata and save the processed data to a file by the name training_data.test
	"""
	print("Creating preprocessed trainingData. Using stopwords? ", use_stop_words)
	if use_stop_words:
		trainingdata = data_handler.get_initialized_train_data(use_stop_words)
	else:
		trainingdata = data_handler.get_initialized_train_data()
	file_handler.save_object(trainingdata, "training_data.test")
	print("Created training_data.test...")
	print("Data has been processed and written to training_data.test.")


def create_testdata_files():
	"""
	This function will process the test_data and save the processed data to a file by the name test_data.test
	"""
	print("Creating preprocessed testData...")
	test_data = data_handler.get_intitialized_test_data()
	file_handler.save_object(test_data, "test_data.test")
	print("Created test_data.test...")
	print("Data has been processed and written to test_data.test.")


def test_prediction_with_loaded_file():
	"""
	This test will attempt to predict the test_data, using the preprocessed data
	Throws FileNotFoundError if the preprocessed data cant be found
	:return:
	"""
	print("Running test_prediction_with_loaded_file...")
	start_time = time.time()
	try:
		training_data = file_handler.load_object("training_data.test")
		test_data = file_handler.load_object("test_data.test")
		results = predict.predict_test_reviews(training_data, test_data)
		print(results)
		number_of_reviews = 25000
		print(str(
			(results["correct_predictions"] - number_of_reviews) / number_of_reviews * (
				100) * -1) + "% is the error rate ")
		end_time = time.time()
		print("Test is complete.")
		print("Test took: " + str(round(end_time - start_time, 2)) + " sec")
	except FileNotFoundError as e:
		print("Exception occoured, please create the test files first then run this again: ", e)


def test_stop_words():
	"""
	First run regular prediction on test set, then do one using stopwords
	"""
	start_time = time.time()
	testing_two_predictions()  # WITHOUT STOPWORDS
	testing_two_predictions(use_stop_words = True)
	end_time = time.time()
	print("Both tests are complete.")
	print("Tests took: " + str(round(end_time - start_time, 2)) + " sec in total")


def big_stop_word_test():
	"""
	This test will first process the training and test data, then try to do predictions.
	The training set will be using stopwords
	"""
	start_time = time.time()
	try:
		training_data = file_handler.load_object("training_data.test")
		test_data = file_handler.load_object("test_data.test")
		results = predict.predict_test_reviews(training_data, test_data)
		print(results)
		number_of_reviews = 25000
		print(str(
			(results["correct_predictions"] - number_of_reviews) / number_of_reviews * (
				100) * -1) + "% is the error rate ")
		end_time = time.time()
		print("Test is complete.")
		print("Test took: " + str(round(end_time - start_time, 2)) + " sec")
	except FileNotFoundError as e:
		print("Exception occoured: ", e)
		print("Attempting to process data and then trying again.")
		create_trainingdata_files(use_stop_words = True)
		create_testdata_files()
		big_stop_word_test()
