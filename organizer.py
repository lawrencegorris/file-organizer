import os
import shutil
from util import helper
from util import file_formats

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
    current_directory = os.getcwd()
    for item in directory:
        if (os.path.isfile(item)):
            item_extension = os.path.splitext(item)[1]
            for format in file_formats.formats:
                if (item_extension in format):
                    helper.CheckForDirectory(format[0])
                    source = os.path.join(current_directory, item)
                    destination_path = os.path.join(current_directory, format[0])
                    destination = os.path.join(destination_path, item)
                    shutil.move(source, destination)
                    print(f"Moving: {item}")
                    print(f"To: {destination}")
                    
                    
# Sorts files in directories for all different file extensions (.txt, .jpg, .png, .mpv, .avi)
#def OrganizeAccordingToExtension(): 