import os

def m(matrix):
    n = len(matrix)
    matching_indices = []
    
    for k in range(n):
        is_match = True
        for j in range(n):
            if matrix[k][j] != matrix[j][k]:
                is_match = False
                break
        
        if is_match:
            matching_indices.append(k)
            
    return matching_indices

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

