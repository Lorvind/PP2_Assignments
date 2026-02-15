class Lesson:
    def __init__(self, time, room):
        self.time = time
        self.room = room

math = Lesson("15:00", "406")

print(math.time, math.room)