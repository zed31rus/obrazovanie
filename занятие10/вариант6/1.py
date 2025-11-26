import os

def m(matrix):
    n = len(matrix)
    if n == 0:
        return
    m = len(matrix[0])

    with open(answer_path, 'a') as file:
        for i in range(n):
            file.write(str((f"Строка {i}: {max(matrix[i])}")))
        
            for j in range(m):
                column = [matrix[i][j] for i in range(n)]
                file.write(f"Столбец {j}: {min(column)}")


script_dir = os.path.dirname(os.path.abspath(__file__))
in_path = os.path.join(script_dir, 'in.txt')
answer_path = os.path.join(script_dir, 'answer.txt')

matrix = []
with open(in_path, 'r') as file:
    for line in file:
        row = list(map(float, line.strip().split()))
        matrix.append(row)


m(matrix)
