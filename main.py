import cli
import os
import fileHandler

path = None


def setPath():
	"""
	Function will ask for the user to input the path to the data, if test and train is found to be in the directory it
	will save the path to config.path. Keeps looping until a proper path is given.
	"""
	directoryNames = []
	path = input(
		"Please give the location of the directory. Just copypaste it in. For example: C:\\Users\\user\\Documents\\GitHub\\Group-Assignment\\Data \n")
	properLocation = False
	try:

		for entry in os.scandir(path):
			directoryNames.append(entry.name)
	except Exception as e:
		print(e)
		setPath()

	if "test" in directoryNames and "train" in directoryNames:  # check if test and train is found in the directory
		properLocation = True

	if properLocation:
		fileHandler.save_object(path, "path.config")
		print(
			"test and train was found in the directory. Saving the path to path.config for future use. You can change this path later.")
	else:
		print("Could not locate test and train in the directory. Please try again.")
		setPath()


def checkPath():
	"""
	Function will attempt to load path.config and set path variable to the path in path.config
	:return: True if successful, False if path.config doesn't exist
	"""
	global path
	print("Attempting to locate path to data directory")
	try:
		path = fileHandler.load_object("path.config")
	except Exception as e:
		print(e)
		return False
	return True


def get_path():
	"""
	This returns the path to the dataset directory
	:return: the path
	"""
	path = fileHandler.load_object("path.config")
	return path


if __name__ == '__main__':
	if checkPath() is False:  # check if path.config can be located. If it can't it will allow the user to paste in location of the dataset
		setPath()
	else:
		print("Path located as " + path)
	while True:  # it will run until you enter exit.
		command = input("Please input a command. Type help for a list of options\n")
		cli.command(command)
