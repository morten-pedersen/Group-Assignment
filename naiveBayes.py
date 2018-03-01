import directoryExplorer
import numpy as np
import os

posTrainPath = os.getcwd() + "\\Data\\train\\pos\\"  # relative path to positive train positive reviews, make sure data folder is in same directory as this py file.
negTrainPath = os.getcwd() + "\\Data\\train\\neg\\"

posTrainFiles = directoryExplorer.getfilelist(posTrainPath)  # list of files
negTrainFiles = directoryExplorer.getfilelist(negTrainPath)  # list of files
vocabulary = list
posWords = None
negWords = None


def addWords(path):
	return path


posTrainPathList = directoryExplorer.getfilelist(posTrainPath)
posWords = directoryExplorer.getwords(posTrainPathList)
# print(posTrainFiles)
# posTrainFiles.pop()
print("hello")
# print(addWords())
