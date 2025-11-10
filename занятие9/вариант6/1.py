def m(matrix):
    n = len(matrix)
    if n == 0:
        return
    m = len(matrix[0])

    for i in range(n):
        print(f"Строка {i}: {max(matrix[i])}")
    
    for j in range(m):
        column = [matrix[i][j] for i in range(n)]
        print(f"Столбец {j}: {min(column)}")