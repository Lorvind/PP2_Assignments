def quiet(s):
    s = s.lower()
    print(s)

def yell(s):
    s = s.upper()
    print(s)

s = input("Enter a sentence:" )
command = input("Enter q or y: ")

match command:
    case "q":
        s = quiet(s)
    case "y":
        s = yell(s)
    case _:
        print(s)