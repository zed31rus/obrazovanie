arr = [1, 2, 3, 2, 4, 1, 5]
duplicates = {}

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] == arr[j]:
            if arr[i] not in duplicates:
                duplicates[arr[i]] = [i, j]
            else:
                duplicates[arr[i]].append(j)

for value, indices in duplicates.items():
    print(f"Элемент {value} повторяется на индексах {indices}")
