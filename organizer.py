import os
from util import helper

# Run without creating/writing to log file
def RunOrganizerWithoutLogging():
    helper.ClearScreen()

    helper.ShowMessage("Running program without logging...")
    helper.PrintEmptyLine()

    helper.ShowMessage("Choose how you want your files to be organized.")
    helper.ShowOrganizeOptions()
    helper.PrintEmptyLine()
    organizeOption = helper.ReadOptionInt()

    while organizeOption not in helper.validOrganizeOptions:
        helper.ShowErrorMessage("Not a valid option. Choose how you want your files to be organized.")
        helper.ShowOrganizeOptions()
        organizeOption = helper.ReadOptionInt()
    
    match organizeOption:
        case 1: 
            OrganizeAccordingToType()
        #case 2: OrganizeAccordingToExtension()
    
# Run with creation of or writing to log file
def RunOrganizerWithLogging():
    print("To be implemented later...")

# Sorts files in general directories based on type (document, image, video)
def OrganizeAccordingToType():
    currentUser = os.getlogin()
    os.chdir(f"C:/Users/{currentUser}/Downloads")
    directory = os.listdir()
    for item in directory:
        if (os.path.isfile(item)):
            print(f"{item} is a file")
        else:
            print(f"{item} is a directory")




# Sorts files in directories for all different file extensions (.txt, .jpg, .png, .mpv, .avi)
#def OrganizeAccordingToExtension(): 
    #