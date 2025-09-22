def countEqual(a, b, c) :
    if a == b == c:
        return 3
    elif a == b or b == c or a == c:
        return 2
    else:
        return 0 

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

print(countEqual(a, b, c))