from util import helper
import organizer

def Main():
    helper.ClearScreen()

    # Startup screen
    helper.ShowMessage("Choose what you want to do.")
    helper.PrintEmptyLine()
    helper.ShowMenuOptions(helper.startup_menu_options)
    program_option = helper.ReadOptionInt()

    # Validate chosen option
    while program_option not in helper.valid_program_options:
        helper.ShowErrorMessage("Not a valid option. Choose what you want to do.")
        program_option = helper.ReadOptionInt()

    # Handle chosen option
    match program_option:
        case 1: 
            organizer.RunOrganizerWithoutLogging()
        case 2: 
            organizer.RunOrganizerWithLogging()
        case 3: 
            helper.ShowMessage("Goodbye.")
            exit
    
if __name__ == '__main__':
    Main()