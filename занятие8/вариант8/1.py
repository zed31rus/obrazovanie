def divisible_by_own_digits(n):
    result = []
    for i in range(1, n+1):
        digits = [int(d) for d in str(i) if d != '0']
        if digits and all(i % d == 0 for d in digits):
            result.append(i)
    return result

print(divisible_by_own_digits(50))