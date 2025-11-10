def m(matrix):
    N = len(matrix)
    total_sum = 0
    count = 0
    for i in range(N):
        for j in range(i + 1, N):
            if matrix[i][j] > 0:
                total_sum += matrix[i][j]
                count += 1
    return total_sum, count