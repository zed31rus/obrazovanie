def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def twin_primes(n):
    primes = [i for i in range(n, 2*n+1) if is_prime(i)]
    return [(primes[i], primes[i+1]) for i in range(len(primes)-1) if primes[i+1] - primes[i] == 2]

print(twin_primes(10))