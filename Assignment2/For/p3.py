def is_prime(n: int):
    if n < 2:
        return False

    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

nums = list(map(int, input("Enter several numbers: ").split()))

for num in nums:
    if is_prime(num):
        print(num, end=' ')
        continue
    print(0, end=' ')