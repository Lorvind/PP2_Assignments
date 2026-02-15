class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def move(self, x: float, y: float):
        self.x += x
        self.y += y

    def show_position(self):
        print(f"x: {self.x} y: {self.y}")

x, y = list(map(float, input("Enter initial position: ").split()))

point = Point(x, y)

x, y = list(map(float, input("Enter movement vector: ").split()))

point.move(x, y)

point.show_position()