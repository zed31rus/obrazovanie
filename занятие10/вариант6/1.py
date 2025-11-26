def m(matrix):
    n = len(matrix)
    if n == 0:
        return
    m = len(matrix[0])

    for i in range(n):
        print(f"Строка {i}: {max(matrix[i])}")
    
    with open('./in.txt', 'r') as file:
        for j in range(m):
            column = [matrix[i][j] for i in range(n)]
            file.write(f"Столбец {j}: {min(column)}")

matrix = []
with open('./in.txt', 'r') as file:
    for line in file:
        row = list(map(float, line.strip().split()))
        matrix.append(row)

m(matrix)