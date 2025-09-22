def can_break(n, m, k):
    return True if k < n*m and ( k % n == 0 or k % m == 0) else False

n = int(input("n: "))
m = int(input("m: "))
k = int(input("k: "))

print(can_break(n, m, k))