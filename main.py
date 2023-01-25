import os
from util import helper
from organizer import *

def Main():
    # Clear screen
    os.system('cls')

    # Startup screen
    helper.ShowMessage("Choose what you want to do.")
    helper.PrintEmptyLine()
    helper.ShowProgramOptions()
    programOption = helper.ReadOptionInt()

    # Validate chosen option
    while programOption not in helper.validOptions:
        helper.ShowErrorMessage("Not a valid input. Choose what you want to do.")
        programOption = helper.ReadOptionInt()

    # Handle chosen option
    match programOption:
        case 1: RunOrganizerWithoutLogging()
        case 2: RunOrganizerWithLogging()
        case 3: helper.ShowMessage("Goodbye.")
    
Main()