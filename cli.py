import os

from stop_words import get_stop_words

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
		stopwords		- learn more about stopwords
		"""

	stopwordsinfo = "Stop words are words that doesn't have any negative or positive meaning.\n" \
					"It can be helpful to use stopwords to remove data that shouldn't impact the prediction.\n" \
					"It can help performance and has an impact on the result."

	stopwordcommands = """				Available commands are:
		help			- lists the commands
		commands		- lists the commands
		info			- lists info about stopwords
		back			- go back to prevous section
		clear			- clear the window
		liststopwords	- lists the stopwords
		"""
	# TODO add more commands
	if command == "exit" or command == "close" or command == "stop":
		quit()
	elif command == "runtest":
		done = False
		clearWindow()
		while not done:
			testToRun = input("Which function do you want to run? This is not case sensitive. Type back to return\n"
							  "preProcessTrainingdata\n"
							  "preProcessTestData\n"
							  "testPredictionWithLoadedFile\n"
							  "savingAndLoadingTests\n"
							  "cleanup   -    this will remove all .test files\n"
							  "predictionTests\n"
							  "testingPredictions\n"
							  "testingTestDataProcessing\n"
							  "testPredictTestReviews\n"
							  "testStopWords\n"
							  "bigStopWordTest\n")
			testToRun = testToRun.lower()
			# TODO add descriptions to tests and clean up
			print("Attempting to run ", testToRun)
			if testToRun == "preProcessTrainingdata".lower():
				testing.createTrainingdataFiles()

			elif testToRun == "back":
				done = True
				print("Returning to previous section...")

			elif testToRun == "preProcessTestData".lower():
				testing.createTestdataFiles()

			elif testToRun == "testPredictionWithLoadedFile".lower():
				testing.testPredictionWithLoadedFile()

			elif testToRun == "savingAndLoadingTests".lower():
				testing.savingAndLoadingTests()

			elif testToRun == "cleanup".lower():
				testing.cleanupFilesFromTests()

			elif testToRun == "predictionTests".lower():
				testing.predictionTests()

			elif testToRun == "testingPredictions".lower():
				testing.testingTwoPredictions()

			elif testToRun == "testingTestDataProcessing".lower():
				testing.testingTestDataProcessing()

			elif testToRun == "testPredictTestReviews".lower():
				testing.testPredictTestReviews()

			elif testToRun == "testStopWords".lower():
				testing.testStopWords()

			elif testToRun == "bigStopWordTest".lower():
				testing.bigStopWordTest()

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

			elif userInput == "liststopwords":
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
