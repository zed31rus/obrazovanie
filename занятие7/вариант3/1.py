D = list(map(float, input("Введите элементы массива через пробел: ").split()))

sum_n_index = sum(D[i] for i in range(1, len(D), 2))

print("Массив D:", D)
print("Сумма элементов с нечётными индексами:", sum_n_index)