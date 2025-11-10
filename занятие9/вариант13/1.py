def m(matrix):
    m = len(matrix)
    if m == 0:
        return 

    for i in range(0, m, 2):
        if matrix[i]:
            print(f"{i}: {min(matrix[i])}")
        else:
            print(f"{i}: ")