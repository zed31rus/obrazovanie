def m(matrix, c, d):
    modified_row_indices = []
    
    for i in range(len(matrix)):
        if c in matrix[i]:
            modified_row_indices.append(i)

            for j in range(len(matrix[i])):
                matrix[i][j] *= d
                
    return modified_row_indices