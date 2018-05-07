import math

import data_handler
import file_handler as fh
from data_handler import get_initialized_train_data, get_intitialized_test_data


def predict_test_reviews(training_data = None, test_data = None):
	"""
	This function will go through all set of test reviews and attempt to predict if it is positive or negative and save the results
	:param training_data: dict that looks like this {"pos_freq":pos_frequency, "neg_freq":neg_frequency,
							  					    "pos_prob":pos_probability, "neg_prob":neg_probability}
	:param test_data: dict that looks like this {"pos_reviews":pos_reviews, "neg_reviews":neg_reviews}
	:return: a dictionary containing the results, key strings are:
	predicted_positive
	predicted_negative
	correct_predictions
	incorrect_predictions
	they contain integers
	"""
	if training_data is None:
		training_data = get_initialized_train_data()
		test_data = get_intitialized_test_data()

	predicted_positive = 0
	predicted_negative = 0
	correct_predictions = 0
	incorrect_predictions = 0
	pos_training_freq = training_data["pos_freq"]
	neg_training_freq = training_data["neg_freq"]
	pos_test_reviews = test_data["pos_reviews"]
	neg_test_reviews = test_data["neg_reviews"]
	counter = 0
	while pos_test_reviews.__len__() > counter:
		current_review = pos_test_reviews[counter]
		pos_prediction = make_class_prediction(text = current_review, pos_or_neg_word_count_dict = pos_training_freq,
		                                       prior_prob = 0.5)
		neg_prediction = make_class_prediction(text = current_review, pos_or_neg_word_count_dict = neg_training_freq,
		                                       prior_prob = 0.5)

		if final_prediction(pos_prediction, neg_prediction) is "positive":
			correct_predictions += 1
			predicted_positive += 1
		else:
			incorrect_predictions += 1
			predicted_negative += 1
		counter += 1
	counter = 0
	while neg_test_reviews.__len__() > counter:
		current_review = neg_test_reviews[counter]
		pos_prediction = make_class_prediction(text = current_review, pos_or_neg_word_count_dict = pos_training_freq,
		                                       prior_prob = 0.5)
		neg_prediction = make_class_prediction(text = current_review, pos_or_neg_word_count_dict = neg_training_freq,
		                                       prior_prob = 0.5)

		if final_prediction(pos_prediction, neg_prediction) is "negative":
			correct_predictions += 1
			predicted_negative += 1
		else:
			incorrect_predictions += 1
			predicted_positive += 1
		counter += 1
	results = {}
	results["predicted_positive"] = predicted_positive
	results["predicted_negative"] = predicted_negative
	results["correct_predictions"] = correct_predictions
	results["incorrect_predictions"] = incorrect_predictions
	return results


# TODO priorprob = log(0.5)????


def make_class_prediction(pos_or_neg_word_count_dict, prior_prob, path = None, text = None):
	"""
	This function will predict if the review is positive or negative, depending on what wordcount dictionary that  is given as arguments
	:param path: the path to the txt file
	:param pos_or_neg_word_count_dict: the positive or negative review wordcounts
	:param prior_prob: the prior probability for positive or negative review, should be around 0.50
	:return: a float with 2 decimals
	"""
	if path is None:
		counted_text = fh.make_word_frequency_dict(text)
	else:
		counted_text = fh.get_words(path = path)  # get the words from the file
		counted_text = fh.make_word_frequency_dict(counted_text)  # make a dict with word frequency in given file
	prediction = 0  # declare prediction
	for word in counted_text:  # go through every word
		if word in pos_or_neg_word_count_dict:  # skip those words we don't have seen before
			prediction += (pos_or_neg_word_count_dict[word] * (counted_text[word] + 1))  # multiply word frequency
	prediction = prior_prob * prediction  # multiply prior probability
	return round(math.log10(prediction), 5)  # return float with 5 decimals TODO: this is probably wrong


def predict_input(text):
	"""
	This function will attempt to predict whether a review that is written by the user is positive or negative.
	:param text: the input from the user
	:return: a set with the results.
	"""
	training_data = data_handler.get_initialized_train_data()
	pos_frequency = training_data["pos_freq"]
	neg_frequency = training_data["neg_freq"]
	pos_probability = training_data["pos_prob"]
	neg_probability = training_data["neg_prob"]
	list_of_words = fh.get_words_from_input(text)
	# countedWords = fh.make_word_frequency_dict(list_of_words)
	pos_prediction = make_class_prediction(pos_frequency, pos_probability, text = list_of_words)
	neg_prediction = make_class_prediction(neg_frequency, neg_probability, text = list_of_words)
	predicted_result = final_prediction(pos_prediction, neg_prediction)
	results = {"It is predicted to be: " + predicted_result, "pos_prediction: " + (str(pos_prediction)),
			   "neg_prediction: " + (str(neg_prediction))}
	return results


def final_prediction(pos_prediction, neg_prediction):
	"""
	Function decides if the prediction is positive or negative
	:param pos_prediction: float number
	:param neg_prediction:  float number
	:return: string
	"""
	if pos_prediction > neg_prediction:
		return "positive"
	else:
		return "negative"

# def final_prediction(text):
#
# 	posPrediction = make_class_prediction(text, pos_frequency, pos_probability, testDictionary)
#
# 	negPrediction = make_class_prediction(text, neg_frequency, neg_probability, testDictionary)
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
