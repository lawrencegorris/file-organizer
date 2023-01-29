class Logger:
    # Writes to log file the start date and time of when the program is run
    def write_new_transfer_title(self, target_directory, current_datetime):
        with open(f'{target_directory}/log.txt', 'a') as log_file:
            log_file.write("***************************************************************************************************** \n")
            log_file.write("*****************************************************************************************************")
            log_file.write("\n")
            log_file.write("New operation started on ")
            log_file.write(current_datetime.strftime("%B %d, %Y - %H:%M:%S"))
            log_file.write("\n \n")
    
    # Writes to log file what moved and to where
    def write_transfer_line(self, target_directory, item, destination):
        with open(f'{target_directory}/log.txt', 'a') as log_file:
            log_file.write(f"Moving: {item} \n")
            log_file.write(f"To: {destination} \n \n")