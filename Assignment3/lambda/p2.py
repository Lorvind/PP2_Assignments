format_text = lambda x: x.lower() + ".txt"

text = input("Enter file names: ").split()
result = list(map(format_text, text))

for entry in result:
    print(entry)