import os

import predictor
import testing


def command(command):
	"""
	This function will take a command and execute the command given, or else it will tell the user the command doesnt exist
	:param command: a string with your command
	"""
	help = """				Available commands are:
		predict			- Attempts to predict whether or not a review is positive or negative. You enter the review. 
		runtest			- allow you to choose a test to run
		exit			- exits the program
		clear			- clears the window
		help			- shows the different commands available
		"""
	# TODO fix text formatting, maybe use spaces instead of tabs? looks wierd in cmd
	if command == "exit" or command == "close" or command == "stop":
		quit()
	elif command == "runtest":
		testToRun = input("Which function do you want to run? This is not case sensitive.\n"
						  "preProcessTrainingdata\n"
						  "preProcessTestData\n"
						  "testPredictionWithLoadedFile\n"
						  "savingAndLoadingTests\n"
						  "cleanupFilesFromTests\n"
						  "predictionTests\n"
						  "testingPredictions\n"
						  "testingTestDataProcessing\n"
						  "testPredicTestReviews")
		testToRun = testToRun.lower()
		print("Attempting to run ", testToRun)
		if testToRun == "preProcessTrainingdata".lower():
			testing.createTrainingdataFiles()
		elif testToRun == "preProcessTestData".lower():
			testing.createTestdataFiles()

		elif testToRun == "testPredictionWithLoadedFile".lower():
			testing.testPredictionWithLoadedFile()

		elif testToRun == "savingAndLoadingTests".lower():
			testing.savingAndLoadingTests()

		elif testToRun == "predictionTests".lower():
			testing.predictionTests()

		elif testToRun =="testingPredictions".lower():
			testing.testingTwoPredictions()

		elif testToRun =="testingTestDataProcessing".lower():
			testing.testingTestDataProcessing()

		elif testToRun=="testPredicTestReviews".lower():
			testing.testPredicTestReviews()



		else:
			print("Couldn't run ", testToRun, " Maybe you spelled it wrong?")
	elif command == "predict":
		userReview = input("Enter your review: ")
		print("Attempting to predict, this may take a while.")
		print("Your input was: " + userReview + "\n")
		result = predictor.predictInput(userReview)
		print(result)


	elif command == "help":
		print(help)

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
