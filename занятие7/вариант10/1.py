arr = list(map(int, input("Введите элементы массива через пробел: ").split()))

duplicates = set(x for x in arr if arr.count(x) > 1)

if duplicates:
    print("Повторяющиеся элементы:", duplicates)
else:
    print("Повторяющихся элементов нет")