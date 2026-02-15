sort_vowel = lambda c: not c in "aiueoy"

s = input("Input a word: ")
s = sorted(s, key=sort_vowel)

print(*s, sep='')