# Valid options upon startup
validOptions = [1, 2, 3]

#def ReadOptionString():
#    string = input()
#    return string

# Gets an int option from input
def ReadOptionInt():
    try:
        value = int(input("Enter a number: "))
        return value
    except:
        ShowErrorMessage("You did not input a number.")

# Prints a message to screen, takes a string as parameter
def ShowMessage(message):
    print(message)

# Prints an error message to screen, takes a string as parameter
def ShowErrorMessage(errorMessage):
    print(errorMessage)

# Prints the options of the program to the screen
def ShowProgramOptions():
    print("1. Run program without logging.")
    print("2. Run program with logging.")
    print("3. Quit the program.")

# Prints an empty line
def PrintEmptyLine():
    print()