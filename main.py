"""
This file is the main file. It is what you run to start the program.
Once set, the path to the location of the dataset can be found in main using get_path()
"""
import os

import cli
import data_handler

path = ""


def set_path():
	"""
	Function will ask for the user to input the path to the data, if test and train is found to be in the directory it
	will save the path to config.path. Keeps looping until a proper path is given.
	"""
	global path
	directory_names = []
	path = input(
		"Please give the location of the directory. Just copypaste it in. For example: C:\\Users\\user\\Documents\\GitHub\\Group-Assignment\\Data \n")
	proper_location = False
	try:

		for entry in os.scandir(path):
			directory_names.append(entry.name)
	except Exception as e:
		print(e)
		set_path()

	if "test" in directory_names and "train" in directory_names:  # check if test and train is found in the directory
		proper_location = True

	if proper_location:
		data_handler.save_object(path, "path.config")
		print(
			"test and train was found in the directory. Saving the path to path.config for future use. You can change this path later.")
	else:
		print("Could not locate test and train in the directory. Please try again.")
		set_path()


def check_path():
	"""
	Function will attempt to load path.config and set path variable to the path in path.config
	:return: True if successful, False if path.config doesn't exist
	"""
	global path
	print("Attempting to locate path to data directory")
	try:
		path = data_handler.load_object("path.config")
	except Exception as e:
		print(e)
		return False
	return True


def get_path():
	"""
	This returns the path to the dataset directory
	:return: the path
	"""
	dir_path = os.path.dirname(os.path.realpath(__file__))
	os.chdir(dir_path)  # changes the current working directory to pathname
	path = data_handler.load_object("path.config")
	return path


if __name__ == '__main__':
	if check_path() is False:  # check if path.config can be located. If it can't it will allow the user to paste in location of the dataset
		set_path()
	else:
		print("Path located as " + path)
	while True:  # it will run until you enter exit.
		command = input("Please input a command. Type help for a list of options\n")
		cli.command(command)
