def primes_till(giv_range):
    primes = [2]
    for i in range(3, giv_range + 1):
        count = 0
        for p in primes:
            if i % p == 0: continue
            if i % p != 0: count += 1
            if count == len(primes): primes.append(i)
    return primes           

def get_LCM(giv_max):
    result = 1
    for p in primes_till(giv_max):
        power = 1
        while p ** power <= giv_max: 
            power += 1
            if p ** power > giv_max: 
                result *= p ** (power - 1)
                break
    return result

print(get_LCM(20))
