import os
import re


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


def getwords(listWithPaths):
	"""
	Function opens the files given in the list of paths finds the words and removes unwanted characters then returns a list of the words
	:param listWithPaths: a list containing the paths of the txt files
	:return: a list containing the words
	"""
	finalListOfWords = [] # this is the list of words that are returned
	for path in listWithPaths:
		with open(path, encoding = "utf8") as file:
			text = file.read().lower()
			file.close()
			text = re.sub('[\'()/!.":,!?]', '', text)  # remove characters we dont want
			text = re.sub('[<>]', ' ', text) # adding space where < or > exists to separate br tags from words
			words = list(text.split())
			for word in words:
				if word.__len__() > 1 and word not in "br":  # check if word is more than one character and is not br which is from the html markup
					finalListOfWords.append(word)
	return finalListOfWords


def makeWordFrequnencyList(listOfWords):
	"""
	Find the frequency of the words in the list given in the parameter, adding them to a dictionary as keys and their
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


# def getWordFrequency(listOfWords):
# 	for word in listOfWords:


def getcommonwords(dicts):  # Maybe useful for testing to see what the most common words are
	"""
	The function finds the most common words in the given dictionaries and returns a list of the most common ones in desc order.
	:param dicts: a list containing the dictionaries
	:return: a list with the most common words
	"""
	commonWords = []
	commonWordsDictionary = {}
	# finding the frequency of the words in all the dictionaries
	for dict in dicts:
		currentDict = dict
		for key in currentDict:
			word = key
			freq = currentDict.get(key)
			if commonWordsDictionary.get(word) is not None:
				commonWordsDictionary[word] = freq + commonWordsDictionary.get(word)
			else:
				commonWordsDictionary[word] = freq

	while commonWordsDictionary.__len__() > 0:  # finding the most common words and add them to the list.
		mostCommon = max(commonWordsDictionary, key = lambda i: commonWordsDictionary[i])
		commonWords.append(mostCommon)
		commonWordsDictionary.__delitem__(mostCommon)
		if commonWords.__len__() == 4:
			return commonWords
	return commonWords
