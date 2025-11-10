def count_numbers(N, digits):
    count = 0
    for i in range(100, N+1):
        if all(int(d) in digits for d in str(i)):
            count += 1
    return count

print(count_numbers(220, {1,2,0}))