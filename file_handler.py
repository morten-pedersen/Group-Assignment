import os
import pickle
import re

from stop_words import get_stop_words


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
	remove_characters(path = None, final_list_of_words = final_list_of_words, text = text)  # removing unwanted characters
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


def make_word_frequency_dict(list_of_words, use_stop_words = False):
	"""
	Find the frequency of the words in the list given in the parameter, adding them to a dictionary as keys with their
	frequency as value
	:param use_stop_words: False by default, if True, words found to be a stopword will not be counted
	:param list_of_words: the list of files
	:return: a dictionary with words as keys and frequency as values
	"""
	dictionary = {}
	if use_stop_words:  # if true, using stopwords
		stop_words = get_stop_words('english')
		for word in list_of_words:  # add the words to a dictionary as keys and their frequency as value.
			if word in dictionary and word not in stop_words:
				dictionary[word] += 1
			elif word not in dictionary and word not in stop_words:
				dictionary[word] = 1
			else:
				pass
		return dictionary
	else:  # Not using stopwords
		for word in list_of_words:  # add the words to a dictionary as keys and their frequency as value.
			if word in dictionary:
				dictionary[word] += 1
			else:
				dictionary[word] = 1
		return dictionary


def get_specific_word(word_count_dict, word):
	"""
	This function will return the value of a word in a dictionary. The value is the number of times it appears in the reviews
	:param word_count_dict: the dictionary will the words and their frequency
	:param word: the word you are looking for
	:return: an integer with the number of times the word appears in the reviews
	"""
	return word_count_dict[word]


def get_common_words(dictionary, words_to_return = None):  # Maybe useful for testing to see what the most common words are
	"""
	The function finds the most common words in the given dictionary and returns a list of the most common ones in desc order.
	:param dictionary: a dictionary with words and their frequency
	:param words_to_return: the number of words to return - default is all the words set an integer to specify
	:return: a list with the most common words
	"""
	common_words = []  # list containing the most common words
	common_words_dictionary = {}
	# finding the frequency of the words in all the dictionaries
	for key in dictionary:
		word = key
		freq = dictionary.get(key)
		if common_words_dictionary.get(word) is not None:
			common_words_dictionary[word] = freq + common_words_dictionary.get(word)
		else:
			common_words_dictionary[word] = freq

	while common_words_dictionary.__len__() > 0:  # finding the most common words and add them to the list.
		mostCommon = max(common_words_dictionary, key = lambda i:common_words_dictionary[i])
		common_words.append(mostCommon)
		common_words_dictionary.__delitem__(mostCommon)
		if words_to_return is not None:
			if common_words.__len__() == words_to_return:  # choose how many words to return
				return common_words
	return common_words
