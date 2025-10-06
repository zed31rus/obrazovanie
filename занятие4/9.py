n = int(input("Введите количество чисел из ряда фибоначчи: "))

a, b = 0, 1
fib_sum = 0

for i in range(n):
    fib_sum += a
    a, b = b, a + b

print(fib_sum)