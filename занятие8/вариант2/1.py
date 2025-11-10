import math

def triangle_area(a):
    return (math.sqrt(3)/4) * a**2

def hexagon_area(a):
    return 6 * triangle_area(a)

print("Площадь правильного шестиугольника:", hexagon_area(4))