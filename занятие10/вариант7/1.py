import os
import math

def m(upper_triangle):
    L = len(upper_triangle)
    n_float = (-1 + math.sqrt(1 + 8 * L)) / 2
    
    if n_float != int(n_float):
        return []

    n = int(n_float)
    matrix = [[0] * n for _ in range(n)]
    
    k = 0
    for i in range(n):
        for j in range(i, n):
            matrix[i][j] = upper_triangle[k]
            matrix[j][i] = upper_triangle[k]
            k += 1
            
    return matrix


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

