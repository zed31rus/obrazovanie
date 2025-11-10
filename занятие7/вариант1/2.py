arr = list(map(float, input("Введите элементы массива через пробел: ").split()))

avg = sum(arr) / len(arr)
avg = round(avg, 1)

result = [avg if x == 0 else x for x in arr]

print("Среднее арифметическое:", avg)
print("Новый массив:", result)