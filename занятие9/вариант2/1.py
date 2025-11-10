def m(matrix):
    n = len(matrix)
    if n == 0:
        return True

    target_sum = sum(matrix[0])

    for i in range(1, n):
        if sum(matrix[i]) != target_sum:
            return False

    for j in range(n):
        col_sum = 0
        for i in range(n):
            col_sum += matrix[i][j]
        if col_sum != target_sum:
            return False
            
    return True