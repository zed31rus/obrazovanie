def is_ordered(row):
    if len(row) <= 1:
        return True
    return row == sorted(row) or row == sorted(row, reverse=True)

def m(matrix):
    global_max = None
    
    for row in matrix:
        if is_ordered(row):
            if not row:
                continue
                
            row_max = max(row)
            if global_max is None or row_max > global_max:
                global_max = row_max
                
    return global_max

matrix = []
with open('./in.txt', 'r') as file:
    for line in file:
        row = list(map(float, line.strip().split()))
        matrix.append(row)

with open('./answer.txt', 'a') as file:
    file.write(m(matrix))