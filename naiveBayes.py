import directoryExplorer
import numpy as np


posTrainPath = "\\Data\\train\\pos\\"  # relative path to positive train positive reviews, make sure data folder is in same directory as this py file.
negTrainPath = "\\Data\\train\\pos\\"

posTrainFiles = list  # list of files
negTrainFiles = list  # list of files

posWords = None
negWords = None


def addWords(path):
	return path


posTrainFiles = directoryExplorer.getTrainData(posTrainPath)
print(posTrainFiles)
# print(addWords())
