import fileHandler
import numpy as np
import os
import math

posTrainPath = os.getcwd() + "\\Data\\train\\pos\\"  # relative path to positive train positive reviews, make sure data folder is in same directory as this py file.
negTrainPath = os.getcwd() + "\\Data\\train\\neg\\"

posTrainFiles = fileHandler.getfilelist(posTrainPath)  # list of files
negTrainFiles = fileHandler.getfilelist(negTrainPath)  # list of files
vocabulary = list
posWords = None
negWords = None


def addWords(path):
	return path


posTrainPathList = fileHandler.getfilelist(posTrainPath)
posWords = fileHandler.getwords(posTrainPathList)
negTrainPathList = fileHandler.getfilelist(negTrainPath)
negWords = fileHandler.getwords(negTrainPathList)
posFrequency = fileHandler.makeWordFrequencyDict(posWords)
negFrequency = fileHandler.makeWordFrequencyDict(negWords)
commonWords = fileHandler.getCommonWords(posFrequency, 50)

#prior probabilities
#negProbability = negTrainPathList / len(posTrainPathList + negTrainPathList)
#posProbability = posTrainPathList / len(posTrainPathList + negTrainPathList)
#print("Prior probability is:", posProbability)


print("Test complete.")
print(commonWords)


