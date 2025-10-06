a = int(input("введите первое число: "))
b = int(input("введите второе число: "))


for i in range(b, a+1):
    if i%2 == 1:
        print(i)