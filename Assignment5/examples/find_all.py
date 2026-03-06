import re

s = input("Input a string with digits: ")

digits = re.findall(r"\d", s)

if digits:
    print(*digits)
else:
    print()