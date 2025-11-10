def armstrong_numbers(k):
    result = []
    for i in range(1, k+1):
        n = len(str(i))
        if sum(int(d)**n for d in str(i)) == i:
            result.append(i)
    return result

print(armstrong_numbers(500))