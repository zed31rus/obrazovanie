def m(matrix, c, d):
    modified_row_indices = []
    
    for i in range(len(matrix)):
        if c in matrix[i]:
            modified_row_indices.append(i)

            for j in range(len(matrix[i])):
                matrix[i][j] *= d
                
    return modified_row_indices

matrix = []
with open('./in.txt', 'r') as file:
    for line in file:
        row = list(map(float, line.strip().split()))
        matrix.append(row)
c = int(input(": "))
d = int(input(": "))
with open('./answer.txt', 'a') as file:
    file.write(m(matrix, c, d))