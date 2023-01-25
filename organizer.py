import os
from util import helper
from util import formats

# Run without creating/writing to log file
def RunOrganizerWithoutLogging():
    helper.ClearScreen()

    helper.ShowMessage("Running program without logging...")
    helper.PrintEmptyLine()

    helper.ShowMessage("Choose how you want your files to be organized.")
    helper.ShowOrganizeOptions()
    helper.PrintEmptyLine()
    organize_option = helper.ReadOptionInt()

    while organize_option not in helper.valid_organize_options:
        helper.ShowErrorMessage("Not a valid option. Choose how you want your files to be organized.")
        helper.ShowOrganizeOptions()
        organize_option = helper.ReadOptionInt()
    
    match organize_option:
        case 1: 
            OrganizeAccordingToType()
        #case 2: OrganizeAccordingToExtension()
    
# Run with creation of or writing to log file
def RunOrganizerWithLogging():
    print("To be implemented later...")

# Sorts files in general directories based on type (document, image, video)
def OrganizeAccordingToType():
    current_user = os.getlogin()
    os.chdir(f"C:/Users/{current_user}/Downloads")
    directory = os.listdir()
    for item in directory:
        if (os.path.isfile(item)):
            item_extension = os.path.splitext(item)[1]


# Sorts files in directories for all different file extensions (.txt, .jpg, .png, .mpv, .avi)
#def OrganizeAccordingToExtension(): 
    #