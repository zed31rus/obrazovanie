def sum_divisors(n):
    return sum(i for i in range(1, n) if n % i == 0)

def amicable_numbers(N):
    pairs = []
    for a in range(2, N+1):
        b = sum_divisors(a)
        if b > a and b <= N and sum_divisors(b) == a:
            pairs.append((a, b))
    return pairs

print(amicable_numbers(300))