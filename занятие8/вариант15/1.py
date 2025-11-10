def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def is_binary_palindrome(n):
    b = bin(n)[2:]
    return b == b[::-1]

def prime_binary_palindromes(n):
    return [i for i in range(2, n+1) if is_prime(i) and is_binary_palindrome(i)]

print(prime_binary_palindromes(50))