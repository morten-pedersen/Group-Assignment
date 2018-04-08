import cli

if __name__ == '__main__':
	while True:  # it will run until you enter exit.
		command = input("Please input a command. Type help for a list of options\n")
		cli.command(command)
