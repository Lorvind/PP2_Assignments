class Counter:
    def __init__(self, count: int, step: int):
        self.count = count
        self.step = step

    def increament(self):
        self.count += self.step


days_without_going_insane = Counter(0, 1)

n = int(input())

for i in range(n):
    days_without_going_insane.increament()

print(days_without_going_insane.count)