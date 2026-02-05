n = int(input("Enter an integer: "))

flag = True

for i in range(2, n // 2):
    if n % i == 0:
        print(f"{n} is divisible by {i}")
        flag = False
        break


if flag:
    print(f"{n} is a prime number")
