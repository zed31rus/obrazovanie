a = int(input("введите первое число: "))
b = int(input("введите второе число: "))

def rrange(a, b):
    if a < b:
        for i in range(a,b+1):
            print(i)
    else:
        for i in range (a, b-1, -1):
            print(i)

rrange(a,b)