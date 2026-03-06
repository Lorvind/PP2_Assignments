import re

s = input()

#sequnce with only capital letters
pattern = "[A-Z]"

upper_cases = re.findall(pattern, s)

print(len(upper_cases))