filter_squares = lambda n: n ** 0.5 == int(n ** 0.5)

numbers = list(map(int, input("Enter several integers: ").split()))
squares = list(filter(filter_squares, numbers))

for num in squares:
    print(num)
