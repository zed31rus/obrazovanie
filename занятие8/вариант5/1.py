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

def subtract_fractions(a, b, c, d):
    num = a*d - b*c
    den = b*d
    return simplify_fraction(num, den)

print("Вычитание дробей:", subtract_fractions(3, 4, 1, 6))