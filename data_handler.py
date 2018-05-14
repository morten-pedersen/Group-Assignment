import os
import pickle
import re
from collections.__init__ import Counter

import main


def get_initialized_train_data():
	"""
	This function will go through the training set and return the positive and negative wordfrequency as well as the their probability.
	:return: A dictionary with the following keys as strings:
	pos_freq - the frequency of words that are in positive reviews
	neg_freq - the frequency of words that are in negative reviews
	pos_prob - the positive probability - amount of positive reviews / total number of reviews
	neg_prob - the negative probability - amount of negative reviews / total number of reviews
	"""
	pos_train_files = get_filelist(main.get_path() + "\\train\\pos\\")  # list of files
	neg_train_files = get_filelist(main.get_path() + "\\train\\neg\\")  # list of files
	pos_words = get_words(pos_train_files)  # list of words
	neg_words = get_words(neg_train_files)  # list of words
	pos_frequency = count_text(pos_words)
	neg_frequency = count_text(neg_words)
	# dictionaries with frequency of words found in negative reviews, use stopwords if true
	pos_probability = pos_train_files.__len__() / (
			pos_train_files.__len__() + neg_train_files.__len__())  # baseline prob
	neg_probability = neg_train_files.__len__() / (pos_train_files.__len__() + neg_train_files.__len__())  # .50ish?
	initialized_training_data = {"pos_freq":pos_frequency, "neg_freq":neg_frequency,
	                             "pos_prob":pos_probability, "neg_prob":neg_probability}
	return initialized_training_data


def get_test_data():
	"""
	Test data is gathered, processed and put in dictionaries
	:return: dict with positive and negative reviews
	Keys:
	pos_reviews - the positive reviews
	neg_reviews - the negative reviews
	"""
	pos_train_files = get_filelist(main.get_path() + "\\test\\pos\\")  # list of files
	neg_train_files = get_filelist(main.get_path() + "\\test\\neg\\")  # list of files
	i = 0
	pos_reviews = {}
	neg_reviews = {}
	while pos_train_files.__len__() is not 0:  # while list is not empty get reviews and put them into a dict
		review = get_words(path = pos_train_files.pop())
		pos_reviews[i] = review  # key is just a number, use __len__() on the dict to find number of reviews later
		i += 1
	i = 0
	while neg_train_files.__len__() is not 0:
		review = get_words(path = neg_train_files.pop())
		neg_reviews[i] = review
		i += 1

	test_data = {"pos_reviews":pos_reviews, "neg_reviews":neg_reviews}
	return test_data


def get_training_words():
	"""
	This function will gather all the training data and return them as a tuple
	:return: a tuple where [0]=pos_words & [1]=neg_words [2]=number of positive reviews, [3]=number of negative reviews
	"""
	pos_train_files = get_filelist(main.get_path() + "\\train\\pos\\")  # list of files
	neg_train_files = get_filelist(main.get_path() + "\\train\\neg\\")  # list of files
	pos_words = get_words(pos_train_files)  # list of words
	neg_words = get_words(neg_train_files)  # list of words
	return pos_words, neg_words, pos_train_files.__len__(), neg_train_files.__len__()


def count_text(words):
	"""
	This function will count the words in the list given
	:param words: a list of words
	:return: a dict where the key is the word and the value is the frequency of the word
	"""
	return Counter(words)


def save_object(obj, filename):
	"""
	This function can take an object and save it to the drive
	# sample usage
	# save_object(test, 'test.pkl')
	:param obj: the object you want to save
	:param filename: the name you want to give to the file that is created
	"""
	dir_path = os.path.dirname(os.path.realpath(__file__))  # get the path to python file
	os.chdir(dir_path)
	with open(filename, 'wb') as output:  # Overwrites any existing file.
		pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)


def load_object(filename):
	"""
	This function loads a saved object from the drive.
	It has to be in the same folder where it is run from
	# sample usage
	# test = load_object("test.pkl")
	:param filename: the filename of the object
	:return: the object
	"""
	with open(filename, 'rb') as input:
		file = pickle.load(input)
	return file


def get_filelist(pathname):
	"""
	The function scans through the given directory looking for .txt files and will put their path's in a list and sort it
	:param pathname: string path to directory
	:return: list with the pathnames as strings
	"""
	os.chdir(pathname)  # changes the current working directory to pathname
	cw = os.getcwd()  # cw is current working directory
	directories = []
	for entry in os.scandir(cw):  # scans through the current working directory
		if ".txt" in entry.name:
			directories.append(entry.path)
	return directories


def get_words_from_input(text):
	"""
	Takes a string of user input and retrieves the words from it without any symbols
	:param text: the user input
	:return: list of words
	"""
	final_list_of_words = []
	remove_characters(path = None, final_list_of_words = final_list_of_words,
	                  text = text)  # removing unwanted characters
	return final_list_of_words


def get_words(list_with_paths = None, path = None, text = None):  # TODO throw error if none of the arguments are None
	"""
	Function opens the files given in the list of paths finds the words and removes unwanted characters then returns a list of the words
	Alternatively it opens the file given in the path and removes unwanted characters
	One of the arguments MUST be None.
	:param text: optional, this is the review
	:param list_with_paths: optional, a list with the paths to the text files, if included, all the text files will be gone through
	:param path: optional, a path to the file, if included, only the file given in the path will be gone through
	:return: a list containing the words
	"""
	final_list_of_words = []  # this is the list of words that are returned
	if path is None:  # multiple files being processed
		for path in list_with_paths:
			remove_characters(path, final_list_of_words)  # removing unwanted characters
		return final_list_of_words
	else:  # one file being processed
		remove_characters(path, final_list_of_words)  # removing unwanted characters
	return final_list_of_words


def remove_characters(path, final_list_of_words, text = None):
	"""
	Function removes character from the file given in the path and appends the words to the list of words
	:param path: the path to the file
	:param final_list_of_words: the list containing the files
	:return: Nothing
	"""
	if text is None:  # Processing a txt file
		with open(path, encoding = "utf8") as file:  # TODO try except pass??
			text = file.read().lower()
			file.close()
			text = re.sub('[\'()/!.":,!?]', '', text)  # remove characters we dont want
			text = re.sub('[<>]', ' ', text)  # adding space where < or > exists to separate br tags from words
			words = list(text.split())
			for word in words:
				if word.__len__() > 1 and word not in "br":  # check if word is more than one character and is not br which is from the html markup
					final_list_of_words.append(word)
	else:  # processing input from user in cli
		text = re.sub('[\'()/!.":,!?]', '', text)  # remove characters we dont want
		text = re.sub('[<>]', ' ', text)  # adding space where < or > exists to separate br tags from words
		words = list(text.split())
		for word in words:
			if word.__len__() > 1 and word not in "br":  # check if word is more than one character and is not br which is from the html markup
				final_list_of_words.append(word)


def get_specific_word(word_count_dict, word):
	"""
	This function will return the value of a word in a dictionary. The value is the number of times it appears in the reviews
	:param word_count_dict: the dictionary will the words and their frequency
	:param word: the word you are looking for
	:return: an integer with the number of times the word appears in the reviews
	"""
	return word_count_dict[word]


def get_common_words(dictionary, words_to_return = 20):
	"""
	The function finds the most common words in the given dictionary and returns a list of the most common ones in desc order.
	:param dictionary: a dictionary with words and their frequency
	:param words_to_return: the number of words to return - default is 20 set an integer to specify
	:return: a list with the most common words
	"""
	common_words = []  # list containing the most common words

	# finding the frequency of the words in all the dictionaries
	counter = 1
	while words_to_return > 0:  # finding the most common words and add them to the list.
		mostCommon = max(dictionary, key = lambda i:dictionary[i])
		common_words.append(str(counter) + ". " + str(mostCommon) + ":           " + str(dictionary[mostCommon]))
		dictionary.__delitem__(mostCommon)
		words_to_return -= 1
		counter += 1

	return common_words


def cleanup_files():
	"""
	This function will remove files that were created by the program
	"""
	dir_path = os.path.dirname(os.path.realpath(__file__))  # get the path to python file
	os.chdir(dir_path)

	try:
		os.remove(os.getcwd() + "\\test.dataset")
		print("test.dataset was removed.")
	except Exception as e:
		pass
	try:
		os.remove(os.getcwd() + "\\classifier.trained")
		print("classifier.trained was removed.")
	except Exception as e:
		pass
