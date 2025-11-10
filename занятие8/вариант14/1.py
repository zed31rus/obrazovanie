def count_divisors(n):
    return sum(1 for i in range(1, n+1) if n % i == 0)

def max_divisors(M, N):
    max_count = 0
    result = []
    for i in range(M, N+1):
        c = count_divisors(i)
        if c > max_count:
            max_count = c
            result = [i]
        elif c == max_count:
            result.append(i)
    return result

print(max_divisors(1, 10))