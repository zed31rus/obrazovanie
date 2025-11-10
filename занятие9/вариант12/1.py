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