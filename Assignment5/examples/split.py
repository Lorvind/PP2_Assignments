import re

s = input("Input a string: ")
d = input("Input a pattern for spliting: ")

result = re.split(d, s)

print(*result, sep=',')