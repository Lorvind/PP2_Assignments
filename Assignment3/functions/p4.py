def prime_factors_to_num(*args):
    result = 1

    for factor in args:
        result *= factor

    return result

num = prime_factors_to_num(2, 2, 3, 5, 11)
print(num)