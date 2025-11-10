arr = list(map(int, input("Введите 10 элементов массива через пробел: ").split()))

if len(arr) != 10:
    print("Ошибка! Нужно ввести ровно 10 элементов.")
else:
    print("Пары отрицательных чисел, стоящих рядом:")
    found = False
    for i in range(len(arr)-1):
        if arr[i] < 0 and arr[i+1] < 0:
            print(f"({arr[i]}, {arr[i+1]})")
            found = True
    if not found:
        print("Таких пар нет")