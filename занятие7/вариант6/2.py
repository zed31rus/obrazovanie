arr = list(map(int, input("Введите 10 элементов массива через пробел: ").split()))

if len(arr) != 10:
    print("Ошибка! Нужно ввести ровно 10 элементов.")
else:
    sum_gt5 = sum(x for x in arr if x > 5)
    print("Сумма элементов больше 5:", sum_gt5)