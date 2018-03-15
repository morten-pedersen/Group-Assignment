import fileExplorer
import numpy as np
import os
import math

posTrainPath = os.getcwd() + "\\Data\\train\\pos\\"  # relative path to positive train positive reviews, make sure data folder is in same directory as this py file.
negTrainPath = os.getcwd() + "\\Data\\train\\neg\\"

posTrainFiles = fileExplorer.getfilelist(posTrainPath)  # list of files
negTrainFiles = fileExplorer.getfilelist(negTrainPath)  # list of files
vocabulary = list
posWords = None
negWords = None


def addWords(path):
	return path


posTrainPathList = fileExplorer.getfilelist(posTrainPath)
posWords = fileExplorer.getwords(posTrainPathList)
negTrainPathList = fileExplorer.getfilelist(negTrainPath)
negWords = fileExplorer.getwords(negTrainPathList)
posFrequency = fileExplorer.makeWordFrequencyList(posWords)
negFrequency = fileExplorer.makeWordFrequencyList(negWords)
commonWords = fileExplorer.getCommonWords(frequency, 50)

#prior probabilities
#negProbability = negTrainPathList / len(posTrainPathList + negTrainPathList)
#posProbability = posTrainPathList / len(posTrainPathList + negTrainPathList)
#print("Prior probability is:", posProbability)


print("Test complete.")
print(commonWords)


