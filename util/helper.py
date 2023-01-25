import os

# Clear screen
def ClearScreen():
    os.system('cls')

# Valid options upon startup
validProgramOptions = [1, 2, 3]

# Valid options to sort by
validOrganizeOptions = [1, 2]

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

def ShowOrganizeOptions():
    print("1. Based on general file type (document, image, video, ...)")
    print("2. Based on file extension (.txt, .jpg, .png, .mpv, .avi, ...)")

# Prints an empty line
def PrintEmptyLine():
    print()

