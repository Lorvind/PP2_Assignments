import shutil

file_name = input("Input file name: ")

shutil.copy(file_name, "backup_" + file_name)