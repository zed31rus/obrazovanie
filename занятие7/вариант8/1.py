arr = list(map(float, input("Введите элементы массива через пробел: ").split()))

total_sum = sum(arr)

total_prod = 1
for x in arr:
    total_prod *= x

print("Сумма элементов:", total_sum)
print("Произведение элементов:", total_prod)