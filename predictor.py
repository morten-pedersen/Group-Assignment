import fileExplorer
import naiveBayes
import os
import re


def testText (path): # Opens a single textfile with path
	with open(path, encoding = "utf8") as file:
		text = file.read().lower()
		file.close()
		text = re.sub('[\'()/!.":,!?]', '', text)
		text = re.sub('[<>]', ' ', text)
	return testText()
