import os
import pickle
import re


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


def load_object(fileName):
	"""
	This function loads a saved object from the drive.
	It has to be in the same folder where it is run from
	# sample usage
	# test = load_object("test.pkl")
	:param fileName: the filename of the object
	:return: the object
	"""
	with open(fileName, 'rb') as input:
		file = pickle.load(input)
	return file


def getfilelist(pathname):
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


def getwordsfrominput(text):
	"""
	Takes a string of user input and retrieves the words from it without any symbols
	:param text: the user input
	:return: list of words
	"""
	finalListOfWords = []
	removeCharacters(path = None, finalListOfWords = finalListOfWords, text = text)  # removing unwanted characters
	return finalListOfWords


def getwords(listWithPaths = None, path = None, text = None):  # TODO throw error if none of the arguments are None
	"""
	Function opens the files given in the list of paths finds the words and removes unwanted characters then returns a list of the words
	Alternatively it opens the file given in the path and removes unwanted characters
	One of the arguments MUST be None.
	:param text: optional, this is the review
	:param listWithPaths: optional, a list with the paths to the text files, if included, all the text files will be gone through
	:param path: optional, a path to the file, if included, only the file given in the path will be gone through
	:return: a list containing the words
	"""
	finalListOfWords = []  # this is the list of words that are returned
	if path is None:  # multiple files being processed
		for path in listWithPaths:
			removeCharacters(path, finalListOfWords)  # removing unwanted characters
		return finalListOfWords
	else:  # one file being processed
		removeCharacters(path, finalListOfWords)  # removing unwanted characters
	return finalListOfWords


def removeCharacters(path, finalListOfWords, text = None):
	"""
	Function removes character from the file given in the path and appends the words to the list of words
	:param path: the path to the file
	:param finalListOfWords: the list containing the files
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
					finalListOfWords.append(word)
	else:  # processing input from user in cli
		text = re.sub('[\'()/!.":,!?]', '', text)  # remove characters we dont want
		text = re.sub('[<>]', ' ', text)  # adding space where < or > exists to separate br tags from words
		words = list(text.split())
		for word in words:
			if word.__len__() > 1 and word not in "br":  # check if word is more than one character and is not br which is from the html markup
				finalListOfWords.append(word)


def makeWordFrequencyDict(listOfWords):
	"""
	Find the frequency of the words in the list given in the parameter, adding them to a dictionary as keys with their
	frequency as value
	:param listOfWords: the list of files
	:return: a dictionary with words as keys and frequency as values
	"""
	dictionary = {}
	for word in listOfWords:  # add the words to a dictionary as keys and their frequency as value.
		if word in dictionary:
			dictionary[word] += 1
		else:
			dictionary[word] = 1
	return dictionary


def getCommonWords(dictionary, wordsToReturn = None):  # Maybe useful for testing to see what the most common words are
	"""
	The function finds the most common words in the given dictionary and returns a list of the most common ones in desc order.
	:param dictionary: a dictionary with words and their frequency
	:param wordsToReturn: the number of words to return - default is all the words set an integer to specify
	:return: a list with the most common words
	"""
	commonWords = []  # list containing the most common words
	commonWordsDictionary = {}
	# finding the frequency of the words in all the dictionaries
	for key in dictionary:
		word = key
		freq = dictionary.get(key)
		if commonWordsDictionary.get(word) is not None:
			commonWordsDictionary[word] = freq + commonWordsDictionary.get(word)
		else:
			commonWordsDictionary[word] = freq

	while commonWordsDictionary.__len__() > 0:  # finding the most common words and add them to the list.
		mostCommon = max(commonWordsDictionary, key = lambda i:commonWordsDictionary[i])
		commonWords.append(mostCommon)
		commonWordsDictionary.__delitem__(mostCommon)
		if wordsToReturn is not None:
			if commonWords.__len__() == wordsToReturn:  # choose how many words to return
				return commonWords
	return commonWords
