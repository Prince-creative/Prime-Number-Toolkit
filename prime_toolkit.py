import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def sieve(n):
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False

    for i in range(2, int(math.sqrt(n)) + 1):
        if prime[i]:
            for j in range(i*i, n+1, i):
                prime[j] = False

    return [i for i in range(n+1) if prime[i]]

def prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    if n > 1:
        factors.append(n)
    return factors

if __name__ == "__main__":
    num = int(input("Enter a number: "))

    print("Is Prime:", is_prime(num))
    print("Prime Factors:", prime_factors(num))

    limit = int(input("Generate primes up to: "))
    print("Primes:", sieve(limit))