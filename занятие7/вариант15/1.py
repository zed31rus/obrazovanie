arr = [1, 3, 2, 3, 4, 1, 5]
duplicates = set([x for x in arr if arr.count(x) > 1])
if duplicates:
    print("Повторяющиеся элементы:", duplicates)
else:
    print("Повторяющихся элементов нет")