def m(matrix):
    if not matrix:
        return 0
        
    min_val = matrix[0][0]
    min_row_index = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < min_val:
                min_val = matrix[i][j]
                min_row_index = i
                
    print(f"Мин элемент {min_val} в{min_row_index}")
    return sum(matrix[min_row_index])