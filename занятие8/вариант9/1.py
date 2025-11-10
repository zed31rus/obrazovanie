def sum_of_digits(n):
    return sum(int(d) for d in str(n))

def steps_to_zero(n):
    count = 0
    while n != 0:
        n -= sum_of_digits(n)
        count += 1
    return count

print(steps_to_zero(21))