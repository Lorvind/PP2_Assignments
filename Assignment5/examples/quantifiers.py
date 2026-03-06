import re

s = input()

#Quantifier to get words with 5 or more letters
pattern = r"\b\w{5,}\b"

words = re.findall(pattern, s)

print(*words)