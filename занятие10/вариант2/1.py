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

matrix = []
with open('./in.txt', 'r') as file:
    for line in file:
        row = list(map(float, line.strip().split()))
        matrix.append(row)

with open('./answer.txt', 'a') as file:
    file.write(m(matrix))
