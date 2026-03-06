import re

def repeat(c: re.match):
    return c.group() * 2

s = input()

result = re.sub(r"\d", repeat, s)

print(result)