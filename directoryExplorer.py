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
	finalListOfWords = []
	for path in listWithPaths:
		with open(path, encoding = "utf8") as file:
			text = file.read().lower()
			file.close()
			text = re.sub('[^a-z\ \']+', "", text)
			words = list(text.split())
			for word in words:
				if word.__len__() > 1:
					finalListOfWords.append(word)
	return finalListOfWords


def getwordfreqs(pathname):
	"""
	Find the frequency of the words in the file in the given parameter, adding them to a dictionary as keys and their
	frequency as value
	:param pathname: the path directly to the file, including .txt
	:return: a dictionary with words as keys and frequency as values
	"""
	file = open(pathname)  # open file
	listOfWords = re.findall(r'\w+', file.read().lower())  # find the words and put them in a list
	file.close()  # close file
	dictionary = {}
	for word in listOfWords:  # add the words to a dictionary as keys and their frequency as value.
		if word in dictionary:
			dictionary[word] += 1
		else:
			dictionary[word] = 1

	return dictionary


def getcommonwords(dicts):
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
