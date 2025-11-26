def m(matrix):
    if not matrix:
        return 0
        
    min_val = matrix[0][0]
    min_row_index = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < min_val:
                min_val = matrix[i][j]
                min_row_index = i
                
    return f'''Мин элемент {min_val} в{min_row_index}
     {sum(matrix[min_row_index])}'''

matrix = []
with open('./in.txt', 'r') as file:
    for line in file:
        row = list(map(float, line.strip().split()))
        matrix.append(row)

with open('./answer.txt', 'a') as file:
    file.write(m(matrix))