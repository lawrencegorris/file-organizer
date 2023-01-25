from util import helper
from organizer import *

def Main():
    helper.ClearScreen()

    # Startup screen
    helper.ShowMessage("Choose what you want to do.")
    helper.PrintEmptyLine()
    helper.ShowProgramOptions()
    program_option = helper.ReadOptionInt()

    # Validate chosen option
    while program_option not in helper.valid_program_options:
        helper.ShowErrorMessage("Not a valid option. Choose what you want to do.")
        program_option = helper.ReadOptionInt()

    # Handle chosen option
    match program_option:
        case 1: 
            RunOrganizerWithoutLogging()
        case 2: 
            RunOrganizerWithLogging()
        case 3: 
            helper.ShowMessage("Goodbye.")
    
Main()