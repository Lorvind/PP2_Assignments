numbers = list(map(int, input("Input several integers: ").split()))

evens = filter(lambda x: x % 2 == 0, numbers)

print(*evens)