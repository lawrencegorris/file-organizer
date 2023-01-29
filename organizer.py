import os
import shutil
import datetime
from util import Logger
from util import helper
from util import file_formats

# Run without creating/writing to log file
def RunOrganizerWithoutLogging():

    helper.ClearScreen()

    helper.ShowMessage("Running program without logging...")
    helper.PrintEmptyLine()

    helper.ShowMessage("Choose how you want your files to be organized.")
    helper.ShowMenuOptions(helper.organize_menu_options)
    helper.PrintEmptyLine()
    organize_option = helper.ReadOptionInt()

    while organize_option not in helper.valid_organize_options:
        helper.ShowErrorMessage("Not a valid option. Choose how you want your files to be organized.")
        helper.ShowMenuOptions(helper.organize_menu_options)
        organize_option = helper.ReadOptionInt()
    
    match organize_option:
        case 1: OrganizeAccordingToTypeNoLog()
        case 2: OrganizeAccordingToExtensionNoLog()
        case 3: 
            helper.ShowMessage("Goodbye.")
            exit
    
# Run with creation of or writing to log file
def RunOrganizerWithLogging():
    helper.ClearScreen()

    helper.ShowMessage("Running program with logging...")
    helper.PrintEmptyLine()

    helper.ShowMessage("Choose how you want your files to be organized.")
    helper.ShowMenuOptions(helper.organize_menu_options)
    helper.PrintEmptyLine()
    organize_option = helper.ReadOptionInt()

    while organize_option not in helper.valid_organize_options:
        helper.ShowErrorMessage("Not a valid option. Choose how you want your files to be organized.")
        helper.ShowMenuOptions(helper.organize_menu_options)
        organize_option = helper.ReadOptionInt()
    
    match organize_option:
        case 1: OrganizeAccordingToTypeWithLog()
        case 2: OrganizeAccordingToExtensionWithLog()
        case 3: 
            helper.ShowMessage("Goodbye.")
            exit

# Sorts files in general directories based on type (document, image, video)
def OrganizeAccordingToTypeNoLog():
     # Get current logged in user
    current_user = os.getlogin()

    # Change directory to source of transfer
    os.chdir(f"C:/Users/{current_user}/Downloads")

    # Check if target directory exists - if not creates it
    helper.CheckForDirectory("Organized Files")

    # Create strings for source and target directory for transfer
    original_directory = f"C:/Users/{current_user}/Downloads"
    target_directory = f"C:/Users/{current_user}/Downloads/Organized Files"

    # for each item in the directory, see what format it belongs to and create/move to correct folder
    for item in os.listdir(original_directory):
        if (os.path.isfile(item)):
            item_extension = os.path.splitext(item)[1]
            for format in file_formats.formats:
                if (item_extension in format):
                    helper.CheckForDirectory(os.path.join(target_directory, format[0]))
                    source = os.path.join(original_directory, item)
                    destination_path = os.path.join(target_directory, format[0])
                    destination = os.path.join(destination_path, item)
                    shutil.move(source, destination)
                    helper.ShowMessage(f"Moving: {item}")
                    helper.ShowMessage(f"To: {destination}")
                    helper.PrintEmptyLine()

def OrganizeAccordingToTypeWithLog():
    # Create new instance  of logger class
    logger = Logger.Logger()

    # Get current logged in user and datetime when function is ran
    current_user = os.getlogin()
    current_datetime = datetime.datetime.now()

    # Change directory to source of transfer
    os.chdir(f"C:/Users/{current_user}/Downloads")

    # Check if target directory exists - if not creates it
    helper.CheckForDirectory("Organized Files")

    # Create strings for source and target directory for transfer
    original_directory = f"C:/Users/{current_user}/Downloads"
    target_directory = f"C:/Users/{current_user}/Downloads/Organized Files"
    
    logger.write_new_transfer_title(target_directory, current_datetime)

    # For each item in the directory, see what format it belongs to and create/move to correct folder
    for item in os.listdir(original_directory):
        if (os.path.isfile(item)):
            item_extension = os.path.splitext(item)[1]
            for format in file_formats.formats:
                if (item_extension in format):
                    helper.CheckForDirectory(os.path.join(target_directory, format[0]))
                    source = os.path.join(original_directory, item)
                    destination_path = os.path.join(target_directory, format[0])
                    destination = os.path.join(destination_path, item)
                    shutil.move(source, destination)
                    helper.ShowMessage(f"Moving: {item}")
                    helper.ShowMessage(f"To: {destination}")
                    helper.PrintEmptyLine()
                    logger.write_transfer_line(target_directory, item, destination)
            
# Sorts files in directories for all different file extensions (.txt, .jpg, .png, .mpv, .avi)
def OrganizeAccordingToExtension(): 
    helper.ShowMessage("To be implemented later...")