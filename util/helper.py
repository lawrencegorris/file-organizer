import os

# Clear screen
def ClearScreen():
    os.system('cls')

### LISTS ###

# Valid options upon startup

valid_program_options = [1, 2, 3]

# Valid options to sort by
valid_organize_options = [1, 2, 3]

startup_menu_options = [
    "Run program without logging.",
    "Run program with logging.",
    "Quit the program."
]

organize_menu_options = [
    "Based on general file type (document, image, video, ...",
    "Based on file extension (.txt, .jpg, .png, .mpv, .avi, ...",
    "Quit the program."
]

### HELPER FUNCTIONS ###

### INPUT FUNCTIONS ###

# Gets an int option from input
def ReadOptionInt():
    try:
        value = int(input("Enter a number: "))
        return value
    except:
        ShowErrorMessage("You did not input a number.")

# Gets a string from input
#def ReadOptionString():
#    string = input()
#    return string

### UI FUNCTIONS ###

# Prints an empty line
def PrintEmptyLine():
    print()

# Prints a message to screen, takes a string as parameter
def ShowMessage(message):
    print(message)

# Prints an error message to screen, takes a string as parameter
def ShowErrorMessage(errorMessage):
    print(errorMessage)

# Shows list items from list, takes a list as a parameter
def ShowMenuOptions(option_list):
    counter = 0;
    for option in option_list:
        counter += 1
        print(f"{counter}. {option}")

### OS METHODS ###

# check if directory exists, if not runs MakeDirectory function
def CheckForDirectory(directory_name):
    directory_exists = os.path.exists(directory_name)
    if (directory_exists == False):
        MakeDirectory(directory_name)
        ShowMessage(f"Created directory: {directory_name}")

# Makes a new directory, takes a string as a parameter
def MakeDirectory(directory_name):
    os.mkdir(directory_name)