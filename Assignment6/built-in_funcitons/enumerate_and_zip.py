names = input("Input several names: ").split()

ages = list(map(int, input("Input several ages: ").split()))

for index, (name, age) in enumerate(zip(names, ages), start=1):
    print(f"{index}.{name} {age}")   