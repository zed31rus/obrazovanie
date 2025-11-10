arr = list(map(float, input("Введите элементы массива через пробел: ").split()))

min_abs_value = min(arr, key=abs)

print("Минимальный по модулю элемент:", min_abs_value)