def alternating_case(s):
    result = ""

    for i in range(len(s)):
        if i % 2 == 0:
            result += s[i].upper()
        else:
            result += s[i].lower()

    return result

s = input()

alternated_s = alternating_case(s)

print(alternated_s * 3)