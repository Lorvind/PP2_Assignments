import math

n = int(input("Input number of sides: "))
l = float(input("Input the length of a side: "))

angle1 = math.radians(360/n)
angle2 = (math.pi - angle1) / 2
height = math.tan(angle2) * l / 2

area_of_triangle = l * height / 2
total_area = area_of_triangle * n

print("The area of the polygon is:", total_area)