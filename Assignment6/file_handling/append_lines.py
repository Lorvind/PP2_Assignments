file_name = input("Input the file name: ")

with open(file_name, 'a') as file:
    print("Input new lines or 'q' to quit:\n")
    while True:
        line = input()

        if line == 'q':
            break
        
        line += '\n'
        file.write(line)
        

with open(file_name) as file:
    print(file.read())