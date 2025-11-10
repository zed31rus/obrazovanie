array = list(map(int, input("Введите элементы массива через пробел: ").split()))
print(max(array))
print(*reversed(array))