def counter(n: int):
    while n >= 0:
        yield n
        n -= 1

n = int(input())

print(*counter(n), sep='\n')