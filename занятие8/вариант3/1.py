import math

def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

a1, b1 = 3, 4
a2, b2 = 5, 12

h1 = hypotenuse(a1, b1)
h2 = hypotenuse(a2, b2)

print("Гипотенуза 1:", h1)
print("Гипотенуза 2:", h2)

if h1 > h2:
    print("Первая гипотенуза больше")
else:
    print("Вторая гипотенуза больше")