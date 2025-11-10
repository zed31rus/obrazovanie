def m(matrix, k):
    n = len(matrix)
    if k < 0 or k >= n:
        return
        
    divider = matrix[k][k]
    
    if divider == 0:
        return
    
    for j in range(len(matrix[k])):
        matrix[k][j] /= divider