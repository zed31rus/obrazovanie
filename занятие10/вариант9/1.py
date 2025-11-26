import os

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

script_dir = os.path.dirname(os.path.abspath(__file__))
in_path = os.path.join(script_dir, 'in.txt')
answer_path = os.path.join(script_dir, 'answer.txt')

matrix = []
with open(in_path, 'r') as file:
    for line in file:
        row = list(map(float, line.strip().split()))
        matrix.append(row)

with open(answer_path, 'a') as file:
    file.write(str(m(matrix)))

