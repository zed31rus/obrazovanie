arr = [int(input(f"Введите элемент {i+1}: ")) for i in range(10)]
average = sum(arr) / len(arr)

arr = [1 if x > average else x for x in arr]
print("Преобразованный массив:", arr)