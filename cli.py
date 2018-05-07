import os

from stop_words import get_stop_words
import main
import data_handler
import file_handler
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
		setpath         - allows you to set the path to the directory that contains the data
		"""

	stop_words_info = "Stop words are words that doesn't have any negative or positive meaning.\n"\
	                  "It can be helpful to use stopwords to remove data that shouldn't impact the prediction.\n"\
	                  "It can help performance and has an impact on the result."

	stop_word_commands = """				Available commands are:
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
		data = data_handler.get_initialized_train_data()
		pos_fr = data["pos_freq"]
		neg_fr = data["neg_freq"]
		print(word, " was found ", file_handler.get_specific_word(pos_fr, word), " times in the positive reviews\n")
		print(word, " was found ", file_handler.get_specific_word(neg_fr, word), " times in the negative reviews\n")


	elif command == "setpath":
		main.set_path()

	elif command == "runtest":
		done = False
		clear_window()
		while not done:
			test_to_run = input("Which function do you want to run? Use the numbers to select. Type back to return\n"
			                    "1  - preProcessTrainingdata      - This will prerocess the training data and save it as a .test file\n"
			                    "2  - preProcessTestData          - This will preprocess the test data and save it as a .test file\n"
			                    "3  - test_prediction_with_loaded_file- This will attempt to do the predictions on the testdata using the .test files\n"
			                    "4  - saving_and_loading_tests       - This test will attempt to save data to a .test file, then load it\n"
			                    "5  - cleanup                     - This will remove all .test files\n"
			                    "6  - testingPredictions          - This will attempt to predict one positive and one negative review\n"
			                    "7  - testing_test_data_processing   - no longer exists\n" # TODO REMOVE THIS AND REORDER
			                    "8  - test_predict_test_reviews      - This will attempt to predict all the test reviews, not using preprocessed data\n"
			                    "9  - test_stop_words               - This test will predict one positive and one negative review while using stopwords\n"
			                    "10 - big_stop_word_test             - This test will attempt to predict all the testreviews while using stopwords\n"
			                    "11 - all                         - This will run all the tests.\n")
			test_to_run = test_to_run.lower()
			print("Attempting to run ", test_to_run)
			if test_to_run == "1":
				testing.create_trainingdata_files()

			elif test_to_run == "2":
				testing.create_testdata_files()

			elif test_to_run == "3":
				testing.test_prediction_with_loaded_file()

			elif test_to_run == "4":
				testing.saving_and_loading_tests()

			elif test_to_run == "5":
				testing.cleanup_files_from_tests()

			elif test_to_run == "6":
				testing.testing_two_predictions()

			elif test_to_run == "7":
				print("no longer exists")

			elif test_to_run == "8":
				testing.test_predict_test_reviews()

			elif test_to_run == "9":
				testing.test_stop_words()

			elif test_to_run == "10":
				testing.big_stop_word_test()

			elif test_to_run == "11":
				testing.create_trainingdata_files()
				testing.create_testdata_files()
				testing.test_prediction_with_loaded_file()
				testing.saving_and_loading_tests()
				testing.cleanup_files_from_tests()
				testing.testing_two_predictions()
				testing.test_predict_test_reviews()
				testing.test_stop_words()
				testing.big_stop_word_test()

			elif test_to_run == "back":
				done = True
				print("Returning to previous section...")

			else:
				print("Couldn't run ", test_to_run, " Maybe you spelled it wrong?\n")
	elif command == "predict":
		userReview = input("Enter your review: ")
		print("Attempting to predict, this may take a while.")
		print("Your input was: " + userReview + "\n")
		result = predictor.predict_input(userReview)
		print(result)


	elif command == "help":
		print(help)

	elif command == "stopwords":
		done = False
		print(stop_word_commands)
		while not done:
			user_input = input("Type a command. Type help for a list of options: ")

			if user_input.lower() == "info":
				print(stop_words_info)

			elif user_input == "back":
				print("Going back...")
				done = True

			elif user_input == "help" or user_input == "commands":
				print(stop_word_commands)

			elif user_input == "clear":
				clear_window()

			elif user_input == "listwords":
				stop_words = get_stop_words('english')
				for word in stop_words:
					print(word)
			else:
				print("Did not recognize that command, type help to show a list of commands")


	elif command == "clear":
		clear_window()

	else:  # if a command that doesnt exist is typed in.
		print(help)


def clear_window():
	"""
	This function will write 100 blank lines to clear the window and then use system call.
	Doing both cause pycharm
	:return:
	"""
	cls = lambda:print('\n' * 100)
	cls()
	os.system('cls' if os.name == 'nt' else 'clear')
