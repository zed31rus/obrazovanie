arr = list(map(int, input("Введите элементы массива через пробел: ").split()))

min_value = min(arr)

min_index = arr.index(min_value)

print("Индекс минимального элемента:", min_index)