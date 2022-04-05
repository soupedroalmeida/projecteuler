from math import sqrt

def d(n):
    i = 1
    result = list()
    while i <= sqrt(n):
        if n % i == 0:
            if n / i == i:
                result.append(i)
            else:
                result.append(i)
                result.append(int(n / i))
        i += 1
    if len(result) > 1: result.pop(1)
    return sum(result)

def check_amicability(a):
    b = d(a)
    if d(b) == a and a != b:
        return True
    return False

final = 0
for i in range(1, 10000):
    if check_amicability(i) == True: final += i

print(final)