from util import helper
from organizer import *

def Main():
    helper.ClearScreen()

    # Startup screen
    helper.ShowMessage("Choose what you want to do.")
    helper.PrintEmptyLine()
    helper.ShowProgramOptions()
    programOption = helper.ReadOptionInt()

    # Validate chosen option
    while programOption not in helper.validProgramOptions:
        helper.ShowErrorMessage("Not a valid option. Choose what you want to do.")
        programOption = helper.ReadOptionInt()

    # Handle chosen option
    match programOption:
        case 1: 
            RunOrganizerWithoutLogging()
        case 2: 
            RunOrganizerWithLogging()
        case 3: 
            helper.ShowMessage("Goodbye.")
    
Main()