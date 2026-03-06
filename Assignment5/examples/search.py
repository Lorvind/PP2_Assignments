import re

s = input("Input a string: ")

p = input("Input a pattern: ")

result = re.search(p, s)

if result:
    print("Yes")
else:
    print("No")