import os

nested_directory = input("Input a nested directory: ")

os.makedirs(nested_directory, exist_ok=True)

print(f"Directories created at: {nested_directory}")