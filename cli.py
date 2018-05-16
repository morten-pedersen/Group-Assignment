import os

from stop_words import get_stop_words
import main
import data_handler
import classifier
import testing


def command(command):
	"""
	This function will take a command and execute the command given, or else it will tell the user the command doesnt exist
	:param command: a string with your command
	"""
	help = """				Available commands are:
		predict	        - Attempts to predict a review by the user 
		run             - allow you to run different parts of the program
		exit            - exits the program
		clear           - clears the window
		help            - shows the different commands available
		wordcount       - Will show how many times a word shows up in the trainingdata, type in the word in the next input
		stopwords       - learn more about stopwords
		setpath         - allows you to set the path to the directory that contains the data
		topwords        - this will list the most common positive or negative words
		candidates      - list the people that contributed to the assignment and how they contributed
		"""

	stop_words_info = "Stop words are words that doesn't have any negative or positive meaning.\n"\
	                  "It can be helpful to use stopwords to remove data that shouldn't impact the prediction.\n"\
	                  "It can help performance and has an impact on the result.\n"\
	                  "The way we handle stop-words is to just skip skip words that are found in the list of stop-words."

	stop_word_commands = """				Available commands are:
		help / commands - lists the commands
		info            - lists info about stopwords
		back            - go back to prevous section
		clear           - clear the window
		listwords       - lists the stopwords
		"""

	if command == "exit" or command == "close" or command == "stop":
		quit()


	elif command == "topwords":

		is_a_number = False
		number_of_words = None
		while not is_a_number:
			number_of_words = input("How many words do you want to see?\n")
			try:
				number_of_words = int(number_of_words)
				is_a_number = True
			except Exception as e:
				print("Please enter a number.")
				pass

		classifier.train()
		common_pos_words = data_handler.get_common_words(classifier.pos_words_dict, number_of_words)
		print("\nPositive words...")
		for item in common_pos_words:
			print(item)
		print("\nNegative words...")
		common_neg_words = data_handler.get_common_words(classifier.neg_words_dict, number_of_words)
		for item in common_neg_words:
			print(item)

	elif command == "wordcount":
		done = False
		while not done:  # You can keep trying different words until you type back
			word = input("Type in the word: ")
			if word == "back":
				done = True
				return  # return to "main menu"
			data = classifier.train()
			pos_fr = data["pos_words_dict"]
			neg_fr = data["neg_words_dict"]
			print(word, " was found ", data_handler.get_specific_word(pos_fr, word), " times in the positive reviews\n")
			print(word, " was found ", data_handler.get_specific_word(neg_fr, word), " times in the negative reviews\n")


	elif command == "setpath":
		main.set_path()

	elif command == "run":
		done = False
		clear_window()
		while not done:  #TODO finish commands
			user_input = input("Which function do you want to run? Use the numbers to select. Type back to return\n"
			                   "1  - train                                                             - This will attempt to load the preprocessed training data from the file, if it can't it will process it and save it as a file \n"
			                   "2  - load test data                                                    - this will load the test data from the file test.data if possible, if it can't it will process the test data and save it as test.data\n"
			                   "3  - predict the test reviews                                          - This will attempt to predict the test reviews\n"
			                   "4  - Predict test review with stopwords                                - This will attempt to predict the test reviews while using stopwords\n"
			                   "5  - cleanup                                                           - This will remove all files created by this program\n"
			                   "back                                                                   - Return back to main menu\n"
			                   "6  - predict training reviews                                          - This will predict the training data\n"
			                   "7  - predict training reviews with stopwords                           - This will predict the training data with stopwords\n"
			                   "8  - predict training reviews with testing dataset                     - This will classify the training reviews, using the testing data for the classifier\n"
			                   "9  - predict training reviews with testing dataset, using stopwords    - This will classify the training reviews, using the testing data for the classifier and stopwords\n"
			                   "10 - predict testing reviews with testing dataset                      - This will classify the testing reviews, using the testing data for the classifier\n"
			                   "11 - predict testing reviews with testing dataset, using stopwords     - This will classify the testing reviews, using the testing data for the classifier and stop-words\n")
			user_input = user_input.lower()
			print("Running ", user_input)
			if user_input == "1":
				classifier.train()
				print("Classifier is ready.")

			elif user_input == "2":
				classifier.load_test_dataset()
				print("Test data is ready.")

			elif user_input == "3":
				print("Attempting to classify the test reviews. This may take a while.")
				testing.test_predict_test_dataset()

			elif user_input == "4":
				print("Attempting to classify the test reviews while using stop-words. This may take a while.")
				testing.test_predict_test_dataset_with_stopwords()

			elif user_input == "5":
				data_handler.cleanup_files()

			elif user_input == "back":
				done = True
				print("Returning to previous section...")

			elif user_input == "6":
				print("Attempting to classify the training reviews. This may take a while.")
				testing.test_predict_train_dataset()

			elif user_input == "7":
				print("Attempting to classify the training reviews with stopwords. This may take a while.")
				testing.test_predict_train_dataset_with_stopwords()
			elif user_input == "8":
				print(
					"Attempting to classify training dataset while using the testing dataset for the classifier. This may take a while.")
				testing.test_predict_train_dataset_with_testing_data()
			elif user_input == "9":
				print(
					"Attempting to classify training dataset while using the testing dataset for the classifier, while using stop-words. This may take a while.")
				testing.test_predict_train_dataset_with_testing_data_with_stopwords()
			elif user_input == "10":
				print(
					"Attempting to classify testing dataset while using the testing dataset for the classifier. This may take a while.")
				testing.test_predict_test_dataset_with_testing_data()

			elif user_input == "11":
				print(
					"Attempting to classify testing dataset while using the testing dataset for the classifier, while using stop-words. This may take a while.")
				testing.test_predict_test_dataset_with_testing_data_using_stopwords()


			else:
				print("Couldn't run ", user_input, " Maybe you spelled it wrong?\n")
	elif command == "predict":
		done = False
		while not done:
			user_input = input("Enter your review or back to return: ")
			if user_input.lower() == "back":
				done = True
				return
			print("Attempting to predict...")
			print("Your input was: " + user_input + "\n")
			result = classifier.predict_input(user_input)
			print(result[0])
			print(result[1])
			print(result[2])


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

	elif command == "candidates":
		print("The candidates are:\n")
		print("110 - wrote all the code and worked on the report")
		print("21  - testing of the code and worked on the report")

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
