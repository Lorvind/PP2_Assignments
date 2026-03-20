file_name = input("Input the file name: ")
sample_data = input("Input text: ")

with open(file_name, "w") as file:
    file.write(sample_data)