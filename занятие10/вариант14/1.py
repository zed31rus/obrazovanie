import os

script_dir = os.path.dirname(os.path.abspath(__file__))
in_path = os.path.join(script_dir, 'in.txt')
answer_path = os.path.join(script_dir, 'answer.txt')

def m(matrix, m):
    n = len(matrix)
    if m < 0 or m >= n:
        
        return

    max_diag_val = matrix[0][0]
    max_diag_row_index = 0
    
    with open(answer_path, 'a') as file:
        for i in range(1, n):
            if matrix[i][i] > max_diag_val:
                max_diag_val = matrix[i][i]
                max_diag_row_index = i
                
        file.write(f"Макc{max_diag_val} в {max_diag_row_index}")

        if m == max_diag_row_index:
            return

        matrix[m], matrix[max_diag_row_index] = matrix[max_diag_row_index], matrix[m]
        file.write(f"{m} и {max_diag_row_index}")
matrix = []
with open(in_path, 'r') as file:
    for line in file:
        row = list(map(float, line.strip().split()))
        matrix.append(row)

(m(matrix))

