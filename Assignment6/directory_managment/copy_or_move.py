import os
import shutil

source_file = input("Input file name: ")

target_directory = input("Input target directory: ")

command = input("Input 'm' to move or 'c' to copy: ")

os.makedirs(target_directory, exist_ok=True)

match command:
    case 'm':
        shutil.move(source_file, target_directory + '/' + source_file)
    case 'c':
        shutil.copy(source_file, target_directory + "/copy_of_" + source_file)