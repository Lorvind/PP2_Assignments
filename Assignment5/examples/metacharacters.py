import re

s = input("Input a string: ")

#Words with digits in the middle, for exapmle a1pha, ch4nge
pattern = r"\b\w+\d+\w+\b"

matches = re.findall(pattern, s)

print(*matches)