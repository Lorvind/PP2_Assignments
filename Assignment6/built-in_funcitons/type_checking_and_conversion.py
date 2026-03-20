user_input = input("Enter a digit as a word or arabic numeral: ")

if user_input.isdigit():
    output = int(user_input)
else:
    digits = {
        "one":1,
        "two":2,
        "three":3,
        "four":4,
        "five":5,
        "six":6,
        "seven":7,
        "eight":8,
        "nine":9,
        "zero":0
    }
    output = digits[user_input.lower()]

print(output)