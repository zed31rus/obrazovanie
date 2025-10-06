n = int(input("введите количество чисел для сложения: "))

sum = 0
for i in range(1, n+1):
    a = int(input(f"введите {i}-ое число: "))
    sum += a
print(sum)