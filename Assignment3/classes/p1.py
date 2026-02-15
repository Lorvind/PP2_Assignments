class Student:
    name: str
    age: int


George = Student
George.name = "George"
George.age = int(input("How old is George? "))

print(George.name, George.age)