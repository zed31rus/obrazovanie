def m(matrix, k):
    if k == 0:
        return 0, None
        
    count = 0
    max_multiple = None
    
    for row in matrix:
        for elem in row:
            if elem % k == 0:
                count += 1
                if max_multiple is None or elem > max_multiple:
                    max_multiple = elem
                    
    return count, max_multiple