import os

script_dir = os.path.dirname(os.path.abspath(__file__))
in_path = os.path.join(script_dir, 'in.txt')
answer_path = os.path.join(script_dir, 'answer.txt')
def m(matrix):
    m = len(matrix)
    if m == 0:
        return 

    with open(answer_path, 'a') as file:
        for i in range(0, m, 2):
            if matrix[i]:
                file.write(f"{i}: {min(matrix[i])}")
            else:
                file.write(f"{i}: ")

script_dir = os.path.dirname(os.path.abspath(__file__))
in_path = os.path.join(script_dir, 'in.txt')
answer_path = os.path.join(script_dir, 'answer.txt')

matrix = []
with open(in_path, 'r') as file:
    for line in file:
        row = list(map(float, line.strip().split()))
        matrix.append(row)

m(matrix)

