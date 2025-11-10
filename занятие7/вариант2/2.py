arr = list(map(int, input("Введите элементы массива через пробел: ").split()))

positive = [x for x in arr if x > 0]
non_positive = [x for x in arr if x <= 0]

print("Положительные элементы:", positive)
print("Остальные элементы:", non_positive)