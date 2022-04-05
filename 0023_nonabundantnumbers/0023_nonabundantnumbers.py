import math

# the max num that can be written as the sum of two abundant numbers is 28123

def getDivisorSum(n):
    divisors = []
    i = 1
    while i <= math.sqrt(n):
        if n % i == 0:
            if n / i == i or n / i == n:
                divisors.append(i)
            else:
                divisors.append(i)
                divisors.append(n / i)
        i += 1
    return sum(divisors)

def isAbundant(n):
    if getDivisorSum(n) > n: return True
    else: return False

def writtenAsSum(n):
    temp = 12
    try:
        while temp <= n // 2:
            if isAbundant(temp) and isAbundant(n - temp): return True
            temp += 1
        return False
    except: return False

total = 0
for i in list(range(28123)):
    if not writtenAsSum(i): total += i

print(total)