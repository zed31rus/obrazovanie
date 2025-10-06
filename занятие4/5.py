a = int(input("введите число для вычесления: "))

sum = 0
for i in range(1, a+1):
    sum += i**3
print(sum)