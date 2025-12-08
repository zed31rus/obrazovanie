def f(x, n):
    if n == 0:
        return 1.0
    return f(x, n - 1) * x / n

print(f(2, 3))