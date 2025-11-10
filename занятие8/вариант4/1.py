def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def simplify_fraction(num, den):
    g = gcd(num, den)
    return num // g, den // g

def divide_fractions(a, b, c, d):
    num = a * d
    den = b * c
    return simplify_fraction(num, den)

print("Деление дробей:", divide_fractions(2, 3, 4, 5))