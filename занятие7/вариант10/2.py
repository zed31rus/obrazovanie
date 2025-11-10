arr = list(map(int, input("Введите 15 элементов массива через пробел: ").split()))

if len(arr) != 15:
    print("Ошибка! Нужно ввести ровно 15 элементов.")
else:
    print("Первоначальный массив:", arr)
    
    transformed = [0 if x < 10 else 1 if x > 20 else x for x in arr]
    print("Преобразованный массив:", transformed)