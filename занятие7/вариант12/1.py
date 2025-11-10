arr = list(map(int, input("Введите элементы массива через пробел: ").split()))

odd_numbers = [x for x in arr if x % 2 != 0]

if odd_numbers:
    min_odd = min(odd_numbers)
    print("Наименьший нечётный элемент:", min_odd)
else:
    print("Нечётных элементов нет")