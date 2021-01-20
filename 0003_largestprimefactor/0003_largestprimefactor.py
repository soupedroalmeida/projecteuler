def prime_factor(n):
    factors = {}
    d = 2
    while n > 1:
        factors[d] = 0
        while n % d == 0:
            factors[d] += 1
            n = n / d
        d += 1
    return factors
keys = prime_factor(12)
print(keys)
