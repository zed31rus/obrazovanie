n = int(input("Введите количество чисел из ряда фибоначчи: "))
k = int(input("Введите точку начала строки чисел фибоначчи: "))

a, b = 0, 1
fib_sum = 0
count = 0

for i in range(1, k + n):
    if i >= k:
        fib_sum += a
        count += 1
    a, b = b, a + b
    if count == n : break

print(fib_sum)