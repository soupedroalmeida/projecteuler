from math import sqrt

def isPrime(number):
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0: return False
    return True

result = (0, None, None)
for b in range(2, 1000):
    if isPrime(b): 
        for a in range(-999, 1000):
            tempResult = None
            n = 0
            while (n ** 2) + (a * n) + b > 0 and isPrime((n ** 2) + (a * n) + b):
                n += 1
            tempResult = (n, a, b)
            if tempResult[0] > result[0]: result = tempResult

print(result[1] * result[2])
