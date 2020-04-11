import os
import sys

while True:
    current_directory_path = os.getcwd()
    prompt_for_command = current_directory_path + ">"
    user_input = input(prompt_for_command)
    command_and_arguments = user_input.split()
    command = command_and_arguments[0]
    
    if "exit" == command:
        sys.exit()
    elif "dir" == command:
        current_directory_message = " Directory of " + current_directory_path
        print(current_directory_message)
        
        directory_entries = os.listdir(current_directory_path)
        for directory_entry in directory_entries:
            print(directory_entry)
    elif "mkdir" == command:
        path_of_directory_to_create = command_and_arguments[1]
        os.mkdir(path_of_directory_to_create)
    elif "cd" == command:
        path_of_directory_to_change_to = command_and_arguments[1]
        os.chdir(path_of_directory_to_change_to)
    elif "type" == command:
        path_of_file_to_print = command_and_arguments[1]
        with open(path_of_file_to_print) as file:
            file_contents = file.read()
            print(file_contents)
    else:
        unknown_command_message = "'" + command + "' is not recognized as an internal or external command."
        print(unknown_command_message)

        

        


