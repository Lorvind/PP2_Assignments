def squares(n: int):
    i = 1
    while i**2 <= n:
        yield i**2
        i += 1

n = int(input())

for square in squares(n):
    print(square)