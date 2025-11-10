def solve14(matrix, m):
    n = len(matrix)
    if m < 0 or m >= n:
        print(f"Ошибка: m={m} вне диапазона [0, {n-1}]")
        return

    max_diag_val = matrix[0][0]
    max_diag_row_index = 0
    
    for i in range(1, n):
        if matrix[i][i] > max_diag_val:
            max_diag_val = matrix[i][i]
            max_diag_row_index = i
            
    print(f"Макc{max_diag_val} в {max_diag_row_index}")
    
    # 2. Поменять строки местами
    if m == max_diag_row_index:
        return
        
    # Python позволяет легко обменивать элементы
    matrix[m], matrix[max_diag_row_index] = matrix[max_diag_row_index], matrix[m]
    print(f"{m} и {max_diag_row_index}")