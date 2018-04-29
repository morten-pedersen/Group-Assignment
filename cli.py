import os

from stop_words import get_stop_words

import dataHandler
import fileHandler
import predictor
import testing


def command(command):
	"""
	This function will take a command and execute the command given, or else it will tell the user the command doesnt exist
	:param command: a string with your command
	"""
	help = """				Available commands are:
		predict			- Attempts to predict a review by the user 
		runtest			- allow you to choose a test to run
		exit			- exits the program
		clear			- clears the window
		help			- shows the different commands available
		wordcount               - Will show how many times a word shows up in the trainingdata, type in the word in the next input
		stopwords		- learn more about stopwords
		"""

	stopwordsinfo = "Stop words are words that doesn't have any negative or positive meaning.\n" \
					"It can be helpful to use stopwords to remove data that shouldn't impact the prediction.\n" \
					"It can help performance and has an impact on the result."

	stopwordcommands = """				Available commands are:
		help / commands - lists the commands
		info            - lists info about stopwords
		back            - go back to prevous section
		clear           - clear the window
		listwords       - lists the stopwords
		"""
	# TODO add more commands
	if command == "exit" or command == "close" or command == "stop":
		quit()

	elif command == "wordcount":
		word = input("Type in the word: ")
		data = dataHandler.getInitializedTrainData()
		posFr = data["posFreq"]
		negFr = data["negFreq"]
		print(word, " was found ", fileHandler.getSpecificWord(posFr, word), " times in the positive reviews\n")
		print(word, " was found ", fileHandler.getSpecificWord(negFr, word), " times in the negative reviews\n")




	elif command == "runtest":
		done = False
		clearWindow()
		while not done:
			testToRun = input("Which function do you want to run? Use the numbers to select. Type back to return\n"
							  "1  - preProcessTrainingdata      - This will prerocess the training data and save it as a .test file\n"
							  "2  - preProcessTestData          - This will preprocess the test data and save it as a .test file\n"
							  "3  - testPredictionWithLoadedFile- This will attempt to do the predictions on the testdata using the .test files\n"
							  "4  - savingAndLoadingTests       - This test will attempt to save data to a .test file, then load it\n"
							  "5  - cleanup                     - This will remove all .test files\n"
							  "6  - testingPredictions          - This will attempt to predict one positive and one negative review\n"
							  "7  - testingTestDataProcessing   - This will test if the testdata can be processed\n"
							  "8  - testPredictTestReviews      - This will attempt to predict all the test reviews, not using preprocessed data\n"
							  "9  - testStopWords               - This test will predict one positive and one negative review while using stopwords\n"
							  "10 - bigStopWordTest             - This test will attempt to predict all the testreviews while using stopwords\n")
			testToRun = testToRun.lower()
			print("Attempting to run ", testToRun)
			if testToRun == "1":
				testing.createTrainingdataFiles()

			elif testToRun == "2":
				testing.createTestdataFiles()

			elif testToRun == "3":
				testing.testPredictionWithLoadedFile()

			elif testToRun == "4":
				testing.savingAndLoadingTests()

			elif testToRun == "5":
				testing.cleanupFilesFromTests()

			elif testToRun == "6":
				testing.testingTwoPredictions()

			elif testToRun == "7":
				testing.testingTestDataProcessing()

			elif testToRun == "8":
				testing.testPredictTestReviews()

			elif testToRun == "9":
				testing.testStopWords()

			elif testToRun == "10":
				testing.bigStopWordTest()

			elif testToRun == "back":
				done = True
				print("Returning to previous section...")

			else:
				print("Couldn't run ", testToRun, " Maybe you spelled it wrong?\n")
	elif command == "predict":
		userReview = input("Enter your review: ")
		print("Attempting to predict, this may take a while.")
		print("Your input was: " + userReview + "\n")
		result = predictor.predictInput(userReview)
		print(result)


	elif command == "help":
		print(help)

	elif command == "stopwords":
		done = False
		print(stopwordcommands)
		while not done:
			userInput = input("Type a command. Type help for a list of options: ")

			if userInput.lower() == "info":
				print(stopwordsinfo)

			elif userInput == "back":
				print("Going back...")
				done = True

			elif userInput == "help" or userInput == "commands":
				print(stopwordcommands)

			elif userInput == "clear":
				clearWindow()

			elif userInput == "listwords":
				stop_words = get_stop_words('english')
				for word in stop_words:
					print(word)
			else:
				print("Did not recognize that command, type help to show a list of commands")


	elif command == "clear":
		clearWindow()

	else:  # if a command that doesnt exist is typed in.
		print(help)


def clearWindow():
	"""
	This function will write 100 blank lines to clear the window and then use system call.
	Doing both cause pycharm
	:return:
	"""
	cls = lambda:print('\n'*100)
	cls()
	os.system('cls' if os.name == 'nt' else 'clear')
