arr = list(map(int, input("Введите элементы массива через пробел: ").split()))

max_value = max(arr)

max_index = arr.index(max_value)

print("Максимальный элемент:", max_value)
print("Порядковый номер (индекс):", max_index)