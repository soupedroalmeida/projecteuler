import math
from itertools import combinations

def coinSums():
    possibleCoins = (1, 2, 5, 10, 20, 50, 100, 200)
    result = 0
    temp = 0
    count = 0

    for i in range(1, len(possibleCoins) + 1):
        result += math.factorial(len(possibleCoins)) / (math.factorial(i) * math.factorial(abs(len(possibleCoins) - i)))

    for i in range(1, len(possibleCoins) + 1):
        comb = list(combinations(possibleCoins, i))
        for j in range(len(comb)):
            for k in range(i):
                temp += comb[j][k]
            if temp <= possibleCoins[-1]: # adopt an ordered possibleCoins
                print(comb[j])
                print(temp)
                count += 1
            temp = 0

    return result

coinSums()