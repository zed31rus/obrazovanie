def m(matrix):
    if not matrix:
        print("Матрица пуста")
        return
    
    row_sums = [sum(row) for row in matrix]

    min_sum = min(row_sums)
    max_sum = max(row_sums)

    min_index = row_sums.index(min_sum)
    max_index = row_sums.index(max_sum)

    return f"""Строка с МИН. суммой (индекс {min_index}, сумма {min_sum}): 
    {matrix[min_index]}
    Строка с МАКС. суммой (индекс {max_index}, сумма {max_sum}): 
    {matrix[max_index]}"""

matrix = []
with open('./in.txt', 'r') as file:
    for line in file:
        row = list(map(float, line.strip().split()))
        matrix.append(row)

with open('./answer.txt', 'a') as file:
    file.write(m(matrix))
