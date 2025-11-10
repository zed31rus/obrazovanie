arr = [3, 7, 2, 9, 4]
max_index = arr.index(max(arr))
min_index = arr.index(min(arr))

arr[max_index], arr[min_index] = arr[min_index], arr[max_index]
print("Массив после обмена:", arr)