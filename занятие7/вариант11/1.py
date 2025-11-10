arr = list(map(int, input("Введите элементы массива через пробел: ").split()))

even_numbers = [x for x in arr if x % 2 == 0]

if even_numbers:
    max_even = max(even_numbers)
    print("Наибольший чётный элемент:", max_even)
else:
    print("Чётных элементов нет")