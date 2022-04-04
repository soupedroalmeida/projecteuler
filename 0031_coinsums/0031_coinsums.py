import math
from itertools import combinations

def coinSums(uCoins, goal):
    cond = False
    if sum(uCoins) <= goal: # if the sum of coins in group is less than or equal to the goal
        print("\ncoins used:", uCoins)
        print("remainder:", goal - sum(uCoins))
        cond = True
    return cond

aCoins = (1, 2, 5, 10, 20, 50, 100, 200)
for nCoins in range(1, len(aCoins) + 1): # for each possible number of coins to group
    # nComb is in the form [(1, 2), (1, 5), ..., (50, 100)] for nCoins = 2, for example
    nComb = list(combinations(aCoins, nCoins))

    for i in range(len(nComb)): # for each possible group of coins (pCoins)
        coinSums(nComb[i], 200)