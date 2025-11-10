arr = list(map(float, input("Введите элементы массива через пробел: ").split()))

avg = sum(arr)/len(arr)

arr = [avg if x == 0 else x for x in arr]

print("Массив после замены нулей:", arr)