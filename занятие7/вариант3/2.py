arr = list(map(int, input("Введите 8 элементов массива через пробел: ").split()))

if len(arr) != 8:
    print("Ошибка! Нужно ввести ровно 8 элементов.")
else:
    arr = [x*2 if x < 15 else x for x in arr]

    print("Преобразованный массив:", arr)