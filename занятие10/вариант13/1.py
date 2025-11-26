def m(matrix):
    m = len(matrix)
    if m == 0:
        return 

    with open('./answer.txt', 'a') as file:
        for i in range(0, m, 2):
            if matrix[i]:
                file.write(f"{i}: {min(matrix[i])}")
            else:
                file.write(f"{i}: ")