def evens(n: int):
    for i in range(0, n + 1, 2):
        yield i

n = int(input())

print(*evens(n), sep=',')