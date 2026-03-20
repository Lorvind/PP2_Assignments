import functools

def multiplication_of_odds(x, y):
    if x % 2 == 1 and y % 2 == 1:
        return x * y
    elif x % 2 == 1:
        return x
    else:
        return 1

numbers = list(map(int, input("Input several numbers: ").split()))

product_of_evens = functools.reduce(multiplication_of_odds, numbers)

print(product_of_evens)