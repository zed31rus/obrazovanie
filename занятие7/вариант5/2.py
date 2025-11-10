arr = list(map(int, input("Введите 10 элементов массива через пробел: ").split()))

unique_arr = list(dict.fromkeys(arr))

print("Массив без повторов:", unique_arr)