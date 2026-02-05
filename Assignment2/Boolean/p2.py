def print_a_table(logical_operator):
    a, b = True, True
    print(int(a), int(b), logical_operator(a, b))
    a, b = True, False
    print(int(a), int(b), logical_operator(a, b))
    a, b = False, True
    print(int(a), int(b), logical_operator(a, b))
    a, b = False, False
    print(int(a), int(b), logical_operator(a, b))

print("AND:")
print_a_table(lambda a,b: a and b)
print("OR")
print_a_table(lambda a,b: a or b)
print("XOR")
print_a_table(lambda a,b: a ^ b)
