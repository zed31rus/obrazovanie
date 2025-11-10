def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

A, B = 12, 18
print("НОД:", gcd(A, B))
print("НОК:", lcm(A, B))