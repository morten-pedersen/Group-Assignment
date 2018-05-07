import os

import file_handler as fh
import main

path = main.get_path()


def get_initialized_train_data(use_stop_words = False):
	"""
	This function will go through the training set and return the positive and negative wordfrequency as well as the their probability.
	:return: A dictionary with the following keys as strings:
	pos_freq - the frequency of words that are in positive reviews
	neg_freq - the frequency of words that are in negative reviews
	pos_prob - the positive probability - amount of positive reviews / total number of reviews
	neg_prob - the negative probability - amount of negative reviews / total number of reviews
	"""
	pos_train_files = fh.get_filelist(path + "\\train\\pos\\")  # list of files
	neg_train_files = fh.get_filelist(path + "\\train\\neg\\")  # list of files
	pos_words = fh.get_words(pos_train_files)  # list of words
	neg_words = fh.get_words(neg_train_files)  # list of words
	pos_frequency = fh.make_word_frequency_dict(pos_words, use_stop_words)
	neg_frequency = fh.make_word_frequency_dict(neg_words, use_stop_words)
	# dictionaries with frequency of words found in negative reviews, use stopwords if true
	pos_probability = pos_train_files.__len__() / (pos_train_files.__len__() + neg_train_files.__len__())  # baseline prob
	neg_probability = neg_train_files.__len__() / (pos_train_files.__len__() + neg_train_files.__len__())  # .50ish?
	initialized_training_data = {"pos_freq":pos_frequency, "neg_freq":neg_frequency,
	                           "pos_prob":pos_probability, "neg_prob":neg_probability}
	return initialized_training_data


def get_intitialized_test_data(use_stop_words = False):
	"""
	Test data is gathered, processed and put in dictionaries
	:return: dict with positive and negative reviews
	Keys:
	pos_reviews - the positive reviews
	neg_reviews - the negative reviews
	"""
	pos_train_files = fh.get_filelist(path + "\\test\\pos\\")  # list of files
	neg_train_files = fh.get_filelist(path + "\\test\\neg\\")  # list of files
	i = 0
	pos_reviews = {}
	neg_reviews = {}
	while pos_train_files.__len__() is not 0:  # while list is not empty get reviews and put them into a dict
		review = fh.get_words(path = pos_train_files.pop())
		pos_reviews[i] = review  # key is just a number, use __len__() on the dict to find number of reviews later
		i += 1
	i = 0
	while neg_train_files.__len__() is not 0:
		review = fh.get_words(path = neg_train_files.pop())
		neg_reviews[i] = review
		i += 1

	initialized_test_data = {"pos_reviews":pos_reviews, "neg_reviews":neg_reviews}
	return initialized_test_data
