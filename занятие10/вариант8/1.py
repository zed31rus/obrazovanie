def m(matrix, k):
    n = len(matrix)
    if k < 0 or k >= n:
        return
        
    divider = matrix[k][k]
    
    if divider == 0:
        return
    
    for j in range(len(matrix[k])):
        matrix[k][j] /= divider

matrix = []
with open('./in.txt', 'r') as file:
    for line in file:
        row = list(map(float, line.strip().split()))
        matrix.append(row)

a = int(input(': '))
with open('./answer.txt', 'a') as file:
    file.write(m(matrix, a))