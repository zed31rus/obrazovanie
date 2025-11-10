arr = list(map(int, input("Введите элементы массива через пробел: ").split()))

if len(arr) == 0:
    print("Массив пуст")
else:
    min_index = arr.index(min(arr))
    max_index = arr.index(max(arr))

    arr[min_index], arr[max_index] = arr[max_index], arr[min_index]
    
    print("Массив после перестановки мин. и макс. элементов:", arr)