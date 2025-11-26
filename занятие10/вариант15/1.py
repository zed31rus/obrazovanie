import os

def m(matrix, c, d):
    modified_row_indices = []
    
    for i in range(len(matrix)):
        if c in matrix[i]:
            modified_row_indices.append(i)

            for j in range(len(matrix[i])):
                matrix[i][j] *= d
                
    return modified_row_indices

script_dir = os.path.dirname(os.path.abspath(__file__))
in_path = os.path.join(script_dir, 'in.txt')
answer_path = os.path.join(script_dir, 'answer.txt')

matrix = []
with open(in_path, 'r') as file:
    for line in file:
        row = list(map(float, line.strip().split()))
        matrix.append(row)
c = int(input(": "))
d = int(input(": "))
with open(answer_path, 'a') as file:
    file.write(str(m(matrix, c, d)))