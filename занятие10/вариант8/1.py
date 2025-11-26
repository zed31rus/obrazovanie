import os

def m(matrix, k):
    n = len(matrix)
    if k < 0 or k >= n:
        return
        
    divider = matrix[k][k]
    
    if divider == 0:
        return
    
    for j in range(len(matrix[k])):
        matrix[k][j] /= divider

script_dir = os.path.dirname(os.path.abspath(__file__))
in_path = os.path.join(script_dir, 'in.txt')
answer_path = os.path.join(script_dir, 'answer.txt')

matrix = []
with open(in_path, 'r') as file:
    for line in file:
        row = list(map(float, line.strip().split()))
        matrix.append(row)

a = int(input(': '))
with open(answer_path, 'a') as file:
    file.write(str(m(matrix)))