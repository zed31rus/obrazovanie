import os

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

script_dir = os.path.dirname(os.path.abspath(__file__))
in_path = os.path.join(script_dir, 'in.txt')
answer_path = os.path.join(script_dir, 'answer.txt')

matrix = []
with open(in_path, 'r') as file:
    for line in file:
        row = list(map(float, line.strip().split()))
        matrix.append(row)

with open(answer_path, 'a') as file:
    file.write(str(m(matrix)))
