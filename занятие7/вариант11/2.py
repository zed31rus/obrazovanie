arr = list(map(int, input("Введите элементы массива через пробел: ").split()))

even_less_10 = [x for x in arr if x % 2 == 0 and x < 10]

if even_less_10:
    even_less_10.sort()
    print("Чётные числа меньше 10 в порядке возрастания:", even_less_10)
else:
    print("Таких чисел нет")