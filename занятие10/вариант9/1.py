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

matrix = []
with open('./in.txt', 'r') as file:
    for line in file:
        row = list(map(float, line.strip().split()))
        matrix.append(row)

a = int(input(': '))
with open('./answer.txt', 'a') as file:
    file.write(m(matrix, a))