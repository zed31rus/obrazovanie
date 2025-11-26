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


matrix = []
with open('./in.txt', 'r') as file:
    for line in file:
        row = list(map(float, line.strip().split()))
        matrix.append(row)

with open('./answer.txt', 'a') as file:
    file.write(m(matrix))
