def same_color(x1, y1, x2, y2):
    return True if ((x1 + y1) % 2) == (x2 + y2) % 2 else False

x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))

print(same_color(x1, y2, x2, y2))