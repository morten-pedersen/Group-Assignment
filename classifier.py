import math
import time
import data_handler
from stop_words import get_stop_words

stop_words = get_stop_words('english')  #import and declare the stopwords
#Storing these variables in RAM for better performance
training_data = None
pos_words_dict = None
neg_words_dict = None
positive_review_count = None
negative_review_count = None
prob_positive = None
prob_negative = None
test_pos_reviews = None
test_neg_reviews = None


def predict_input(text):
	"""
	This function will attempt to predict whether a review that is written by the user is positive or negative.
	:param text: the input from the user
	:return: a set with the results.
	"""
	train()  #this will attempt to load from file
	list_of_words = data_handler.get_words_from_input(text)
	pos_prediction = make_class_prediction(list_of_words, pos_words_dict, prob_positive, positive_review_count)
	neg_prediction = make_class_prediction(list_of_words, neg_words_dict, prob_negative, negative_review_count)
	predicted_result = decide_outcome(pos_prediction, neg_prediction)
	if predicted_result == 1:
		predicted_result = "positive"
	else:
		predicted_result = "negative"

	results = []
	results.append("It is predicted to be: " + predicted_result)
	results.append("pos_prediction: " + (str(pos_prediction)))
	results.append("neg_prediction: " + (str(neg_prediction)))
	return results


def make_class_prediction(text, review_wordcount_dict, review_probability, number_of_reviews, use_stop_words = False):
	"""
	This will calculate the positive or negative review's value by looking at the frequency of the words in the training
	data
	:param text: the review as a list
	:param review_wordcount_dict: the frequency of the words as a dictionary where the keys are the words
	:param review_probability: the prior probability
	:param number_of_reviews: the total number of positive or negative reviews
	:return: the predicted value
	"""
	prediction = 1
	if type(text) is list: # if it is a list it is not counted, should just be the case for user input
		text_WC_dict = data_handler.count_text(text)
	else: # it is already counted and does not need to be counted again
		text_WC_dict = text
	divide_with_this = (sum(review_wordcount_dict.values()) + number_of_reviews)
	# to improve performance, this calculation is done once here and called divide_with_this
	# summing up all the values in the dictionary for every word makes the prediction very slow and is not needed.
	if not use_stop_words:
		for word in text_WC_dict:
			prediction += math.log(
				text_WC_dict.get(word, 0) * ((review_wordcount_dict.get(word, 0) + 1) / divide_with_this))
	else:

		for word in text_WC_dict:
			if word not in stop_words:
				prediction += math.log(
					text_WC_dict.get(word, 0) * ((review_wordcount_dict.get(word, 0) + 1) / divide_with_this))
	return prediction * review_probability


def classify(text, use_stop_words = False):
	# P(xi|H) the likelyhood or the probability of predictor (a word) given hypothesis (positive review), adding 1 to
	# smooth the value so we dont multiply the prediction by 0 if the word didn't exist in the training data
	negative_prediction = make_class_prediction(text, neg_words_dict, prob_negative, negative_review_count,
	                                            use_stop_words = use_stop_words)
	positive_prediction = make_class_prediction(text, pos_words_dict, prob_positive, positive_review_count,
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
	if it is unable to do so it will load the data and save it as classifier.trained
	:return:
	"""
	global pos_words_dict, neg_words_dict, positive_review_count, negative_review_count, prob_positive, prob_negative, test_pos_reviews, test_neg_reviews
	start_time = time.time()
	if use_testing_data == False:
		try:
			data = data_handler.load_object("classifier.trained")

			pos_words_dict = data["pos_words_dict"]
			neg_words_dict = data["neg_words_dict"]
			positive_review_count = data["positive_review_count"]
			negative_review_count = data["negative_review_count"]
			prob_positive = data["prob_positive"]
			prob_negative = data["prob_negative"]
		except Exception as e:
			print(
				"Couldn't load test data from the classifier.trained file. Processing the training data now, this may take a while...")
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
		except Exception as e:
			print(
				"Couldn't load test data from the classifier.trained file. Processing the training data now, this may take a while...")
			data = process_training_data(use_testing_data = use_testing_data)
			data_handler.save_object(data, "classifier_from_testing_data.trained")

	final_time = time.time() - start_time
	print("It took: "f'{final_time:.2f}'" seconds to load the classifier\n")  # TODO REMOVE BEFORE SUBMITTING??
	return {
		"pos_words_dict":pos_words_dict,
		"neg_words_dict":neg_words_dict,
		"positive_review_count":positive_review_count,
		"negative_review_count":negative_review_count,
		"prob_positive":prob_positive,
		"prob_negative":prob_negative}


def process_training_data(use_testing_data = False):
	"""
	This will process the training data and prepare it for the classifier
	:return: pos_words_dict, neg_words_dict, positive_review_count,
			negative_review_count, prob_positive, prob_negative
	"""
	global pos_words_dict, neg_words_dict, positive_review_count, negative_review_count, prob_positive, prob_negative

	training_data = data_handler.get_training_words(use_testing_data = use_testing_data)
	pos_words_dict = data_handler.count_text(training_data[0])
	neg_words_dict = data_handler.count_text(training_data[1])
	positive_review_count = training_data[2]
	negative_review_count = training_data[3]
	prob_positive = positive_review_count / (positive_review_count + negative_review_count)
	prob_negative = negative_review_count / (positive_review_count + negative_review_count)
	print("P(y) or the prior positive probability is: ", prob_positive)

	return {
		"pos_words_dict":pos_words_dict,
		"neg_words_dict":neg_words_dict,
		"positive_review_count":positive_review_count,
		"negative_review_count":negative_review_count,
		"prob_positive":prob_positive,
		"prob_negative":prob_negative}


def load_test_dataset(use_training_data = False):
	"""
	This will load the test dataset from test.data if possible, else it will process it and create that file.
	:return:
	"""
	#test reviews
	start_time = time.time()
	global test_pos_reviews, test_neg_reviews

	if use_training_data == False:
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
	return test_pos_reviews, test_neg_reviews


def predict_reviews(use_stop_words = False, predict_training_data = False):
	"""
	Predicts all the test reviews
	:return: a dict with the results, keys are:
	predicted_positive
	predicted_negative
	correct_predictions
	incorrect_predictions
	"""
	load_test_dataset(use_training_data = predict_training_data)
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
		classificiation = classify(current_review, use_stop_words = use_stop_words)
		if classificiation == -1:
			predicted_negative += 1
			incorrect_predictions += 1
		else:
			predicted_positive += 1
			correct_predictions += 1
		counter += 1
	counter = 0

	while neg_test_reviews.__len__() > counter:
		current_review = neg_test_reviews[counter]
		classificiation = classify(current_review, use_stop_words = use_stop_words)
		if classificiation == -1:
			predicted_negative += 1
			correct_predictions += 1
		else:
			predicted_positive += 1
			incorrect_predictions += 1
		counter += 1

	results = {}
	results["predicted_positive"] = predicted_positive
	results["predicted_negative"] = predicted_negative
	results["correct_predictions"] = correct_predictions
	results["incorrect_predictions"] = incorrect_predictions
	return results
