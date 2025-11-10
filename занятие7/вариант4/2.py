arr = list(map(int, input("Введите элементы массива через пробел: ").split()))

odd_numbers = [x for x in arr if x % 2 != 0]

if odd_numbers:
    odd_numbers.sort(reverse=True)
    print("Нечетные элементы в порядке убывания:", odd_numbers)
else:
    print("Нечетных чисел нет")