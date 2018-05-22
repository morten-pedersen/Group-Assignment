"""
This file is responsible for classifying movie reviews
"""
import math
import time

from stop_words import get_stop_words

import data_handler

stop_words = get_stop_words('english')  #import and declare the stopwords
pos_words_dict = None
neg_words_dict = None
positive_review_count = None
negative_review_count = None
prob_positive = None
prob_negative = None
test_pos_reviews = None
test_neg_reviews = None


def predict_input(review):
	"""
	This function will attempt to predict whether a review that is written by the user is positive or negative.
	:param review: the input from the user, a string
	:return: a list with the results
	"""
	review_as_a_list = data_handler.process_words_from_input(review)
	pos_prediction = make_class_prediction(review_as_a_list, pos_words_dict, prob_positive, positive_review_count)
	neg_prediction = make_class_prediction(review_as_a_list, neg_words_dict, prob_negative, negative_review_count)
	predicted_result = decide_outcome(pos_prediction, neg_prediction)
	if predicted_result == 1:
		predicted_result = "positive"
	else:
		predicted_result = "negative"

	results = ["It is predicted to be: " + predicted_result, "pos_prediction: " + (str(pos_prediction)),
	           "neg_prediction: " + (str(neg_prediction))]
	return results


def make_class_prediction(review, review_wordcount_dict, review_probability, number_of_reviews, use_stop_words = False):
	"""
	This will calculate the positive or negative review's value by looking at the frequency of the words in the training
	data
	:param review: the review as a list or a dictionary with words as keys and their frequency as values
	:param review_wordcount_dict: the frequency of the words as a dictionary where the keys are the words
	:param review_probability: the prior probability
	:param number_of_reviews: the total number of positive or negative reviews
	:param use_stop_words: False by default, if True it will ignore words that are stop-words
	:return: the predicted value
	"""
	prediction = 1
	if type(review) is list:  # if it is a list it is not counted, should just be the case for user input
		text_wc_dict = data_handler.count_text(review)
	else:  # it is already counted and does not need to be counted again
		text_wc_dict = review
	divide_with_this = (sum(review_wordcount_dict.values()) + number_of_reviews)
	# to improve performance, this calculation is done once here and called divide_with_this
	# summing up all the values in the dictionary for every word makes the prediction very slow and is not needed.
	if not use_stop_words:  # not using stop-words
		for word in text_wc_dict:
			prediction += math.log(
				text_wc_dict.get(word, 0) * ((review_wordcount_dict.get(word, 0) + 1) / divide_with_this))

	else:  # using stopwords - skipping the words that are stop-words
		for word in text_wc_dict:
			if word not in stop_words:
				prediction += math.log(
					text_wc_dict.get(word, 0) * ((review_wordcount_dict.get(word, 0) + 1) / divide_with_this))
	return prediction * review_probability  #multiply the probability with the prior probability


def classify(review, use_stop_words = False):
	"""
	This function will classify a review
	:param review: the review
	:param use_stop_words: Optional, False by default - if true stop-words will be used
	:return: 1 if positive, -1 if negative
	"""
	negative_prediction = make_class_prediction(review, neg_words_dict, prob_negative, negative_review_count,
	                                            use_stop_words = use_stop_words)
	positive_prediction = make_class_prediction(review, pos_words_dict, prob_positive, positive_review_count,
	                                            use_stop_words = use_stop_words)

	return decide_outcome(positive_prediction, negative_prediction)


def decide_outcome(positive_prediction, negative_prediction):
	"""
	Make the final decision if it is positive or negative
	:param positive_prediction:
	:param negative_prediction:
	:return: -1 if negative 1 if positive
	"""
	if negative_prediction > positive_prediction:
		return -1
	else:
		return 1


def train(use_testing_data = False):
	"""
	This will attempt to load the classifier and declare the variables,
	if it is unable to do so it will process the data and save it as classifier.trained
	:param use_testing_data: Optional, False by default - if true testing data will be used
	:return: a dictionary with the following:
		"pos_words_dict":pos_words_dict,
		"neg_words_dict":neg_words_dict,
		"positive_review_count":positive_review_count,
		"negative_review_count":negative_review_count,
		"prob_positive":prob_positive,
		"prob_negative":prob_negative
	"""
	global pos_words_dict, neg_words_dict, positive_review_count, negative_review_count,\
		prob_positive, prob_negative, test_pos_reviews, test_neg_reviews
	start_time = time.time()
	if not use_testing_data:
		try:
			data = data_handler.load_object("classifier.trained")
			pos_words_dict = data["pos_words_dict"]
			neg_words_dict = data["neg_words_dict"]
			positive_review_count = data["positive_review_count"]
			negative_review_count = data["negative_review_count"]
			prob_positive = data["prob_positive"]
			prob_negative = data["prob_negative"]
		except Exception:
			print(
				"Couldn't load test data from the classifier.trained file."
				" Processing the training data now, this may take a while...")
			data = process_training_data()
			data_handler.save_object(data, "classifier.trained")

	else:  # use testing data to train
		try:
			data = data_handler.load_object("classifier_from_testing_data.trained")
			pos_words_dict = data["pos_words_dict"]
			neg_words_dict = data["neg_words_dict"]
			positive_review_count = data["positive_review_count"]
			negative_review_count = data["negative_review_count"]
			prob_positive = data["prob_positive"]
			prob_negative = data["prob_negative"]
		except Exception:
			print(
				"Couldn't load test data from the classifier_from_testing_data.trained file. "
				"Processing the training data now, this may take a while...")
			data = process_training_data(use_testing_data = use_testing_data)
			data_handler.save_object(data, "classifier_from_testing_data.trained")

	final_time = time.time() - start_time
	print("It took: "f'{final_time:.2f}'" seconds to load the classifier\n")
	return {
		"pos_words_dict": pos_words_dict,
		"neg_words_dict": neg_words_dict,
		"positive_review_count": positive_review_count,
		"negative_review_count": negative_review_count,
		"prob_positive": prob_positive,
		"prob_negative": prob_negative}


def process_training_data(use_testing_data = False):
	"""
	This will process the training data and prepare it for the classifier
	:param use_testing_data: Optional, False by default - if true testing data will be used
	:return: a dictionary with the following:
		"pos_words_dict":pos_words_dict,
		"neg_words_dict":neg_words_dict,
		"positive_review_count":positive_review_count,
		"negative_review_count":negative_review_count,
		"prob_positive":prob_positive,
		"prob_negative":prob_negative
	"""
	global pos_words_dict, neg_words_dict, positive_review_count, negative_review_count, prob_positive, prob_negative

	training_data = data_handler.get_training_data(use_testing_data = use_testing_data)
	pos_words_dict = data_handler.count_text(training_data[0])
	neg_words_dict = data_handler.count_text(training_data[1])
	positive_review_count = training_data[2]
	negative_review_count = training_data[3]
	prob_positive = positive_review_count / (positive_review_count + negative_review_count)
	prob_negative = negative_review_count / (positive_review_count + negative_review_count)
	print("P(y) or the prior positive probability is: ", prob_positive)

	return {
		"pos_words_dict": pos_words_dict,
		"neg_words_dict": neg_words_dict,
		"positive_review_count": positive_review_count,
		"negative_review_count": negative_review_count,
		"prob_positive": prob_positive,
		"prob_negative": prob_negative}


def load_test_dataset(use_training_data = False):
	"""
	This will load the test dataset from test.data if possible, else it will process it and create that file.
	:param use_training_data: Optional, False by default - if true training data will be used
	"""
	start_time = time.time()
	global test_pos_reviews, test_neg_reviews

	if not use_training_data:
		try:
			test_data = data_handler.load_object("test.dataset")
			test_pos_reviews = test_data["pos_reviews"]
			test_neg_reviews = test_data["neg_reviews"]

		except Exception:
			print(
				"Couldn't load test data from the test.dataset file. Processing the test data now, this may take a while.")
			test_data = data_handler.get_test_data()
			test_pos_reviews = test_data["pos_reviews"]
			test_neg_reviews = test_data["neg_reviews"]
			data_handler.save_object(test_data, "test.dataset")
	else:
		try:
			test_data = data_handler.load_object("training.dataset")
			test_pos_reviews = test_data["pos_reviews"]
			test_neg_reviews = test_data["neg_reviews"]

		except Exception:
			print(
				"Couldn't load test data from the training.dataset file. Processing the test data now, this may take a while.")
			test_data = data_handler.get_test_data(use_training_data = use_training_data)
			test_pos_reviews = test_data["pos_reviews"]
			test_neg_reviews = test_data["neg_reviews"]
			data_handler.save_object(test_data, "training.dataset")
	final_time = time.time() - start_time
	print("It took: "f'{final_time:.2f}'" seconds to load the test dataset\n")


def predict_reviews(use_stop_words = False, classify_training_data = False):
	"""
	Predicts all the test reviews
	:param use_stop_words: False by default, if True - stopwords are used
	:param classify_training_data: False by default, if True - the training data will be classified
	:return: a dict with the results, keys are:
	predicted_positive
	predicted_negative
	correct_predictions
	incorrect_predictions
	"""
	load_test_dataset(use_training_data = classify_training_data)
	predicted_positive = 0
	predicted_negative = 0
	correct_predictions = 0
	incorrect_predictions = 0
	counter = 0
	pos_test_reviews = []
	neg_test_reviews = []
	for review in test_pos_reviews:
		pos_test_reviews.append(data_handler.count_text(test_pos_reviews[review]))

	for review in test_neg_reviews:
		neg_test_reviews.append(data_handler.count_text(test_neg_reviews[review]))

	while pos_test_reviews.__len__() > counter:
		current_review = pos_test_reviews[counter]
		classification = classify(current_review, use_stop_words = use_stop_words)
		if classification == -1:
			predicted_negative += 1
			incorrect_predictions += 1
		else:
			predicted_positive += 1
			correct_predictions += 1
		counter += 1
	counter = 0

	while neg_test_reviews.__len__() > counter:
		current_review = neg_test_reviews[counter]
		classification = classify(current_review, use_stop_words = use_stop_words)
		if classification == -1:
			predicted_negative += 1
			correct_predictions += 1
		else:
			predicted_positive += 1
			incorrect_predictions += 1
		counter += 1

	results = {"predicted_positive": predicted_positive, "predicted_negative": predicted_negative,
	           "correct_predictions": correct_predictions, "incorrect_predictions": incorrect_predictions}
	return results
