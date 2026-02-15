class BasicOperator:
    def func(self, a, b):
        return a + b

class Subtractor(BasicOperator):
    def func(self, a, b):
        return a - b

add = BasicOperator()

sub = Subtractor()

x, y = list(map(int, input().split()))

print(add.func(x, y))
print(sub.func(x, y))