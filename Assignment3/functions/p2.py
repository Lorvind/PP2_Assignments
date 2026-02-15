def calculate_distance(x1, y1, x2, y2):
    delta_x = x2 - x1
    delta_y = y2 - y1
    distance = (delta_x**2 + delta_y**2)**0.5

    print(distance)

x1, y1 = list(map(float, input("Enter x y of first point: ").split()))
x2, y2 = list(map(float, input("Enter x y of second point: ").split()))
calculate_distance(x1, y1, x2, y2)