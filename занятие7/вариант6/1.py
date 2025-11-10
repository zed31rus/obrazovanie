arr = list(map(int, input("Введите 10 элементов массива через пробел: ").split()))

if len(arr) != 10:
    print("Ошибка! Нужно ввести ровно 10 элементов.")
else:
    avg = sum(arr)/len(arr)
    less_count = sum(1 for x in arr if x < avg)
    greater_count = sum(1 for x in arr if x > avg)
    
    print("Среднее арифметическое:", avg)
    print("Количество элементов меньше среднего:", less_count)
    print("Количество элементов больше среднего:", greater_count)