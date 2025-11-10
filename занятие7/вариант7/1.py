arr = list(map(int, input("Введите элементы массива через пробел: ").split()))

sum_even_index = sum(arr[i] for i in range(0, len(arr), 2))

prod_odd_index = 1
for i in range(1, len(arr), 2):
    prod_odd_index *= arr[i]

print("Сумма элементов с четными индексами:", sum_even_index)
print("Произведение элементов с нечётными индексами:", prod_odd_index)