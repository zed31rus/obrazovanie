def rectangle_area(x, y):
    return x * y

def right_triangle_area(x, y):
    return 0.5 * x * y

X, Y, Z, T = 3, 4, 5, 6
area = rectangle_area(X, Y) + right_triangle_area(Z, T)
print("Площадь четырехугольника:", area)