def m(matrix):
    if not matrix:
        print("Матрица пуста")
        return
    
    row_sums = [sum(row) for row in matrix]

    min_sum = min(row_sums)
    max_sum = max(row_sums)

    min_index = row_sums.index(min_sum)
    max_index = row_sums.index(max_sum)

    print(f"Строка с МИН. суммой (индекс {min_index}, сумма {min_sum}):")
    print(matrix[min_index])
    print(f"Строка с МАКС. суммой (индекс {max_index}, сумма {max_sum}):")
    print(matrix[max_index])