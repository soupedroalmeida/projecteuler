def primes_till(index):
    primes = [2]
    num = 3
    while len(primes) < index:
        count = 0
        for p in primes:
            if num % p == 0: 
                num += 1
                break
            if num % p != 0: count += 1
            if count == len(primes): 
                primes.append(num)
                num += 1
                break
    return primes

print(primes_till(10001)[10000])
