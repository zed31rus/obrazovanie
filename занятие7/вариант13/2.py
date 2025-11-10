arr = [10, 20, 5, 15, 12, 25, 8, 30]
for i in range(len(arr)):
    if arr[i] < 15:
        arr[i] *= 2

print("Преобразованный массив:", arr)