from itertools import combinations

def checkSum(uCoins, goal):
    result = False
    if sum(uCoins) <= goal: # if the sum of coins in group is less than or equal to the goal
        result = True
    return [result, uCoins, goal - sum(uCoins)] 

def checkComb(uCoins):
    result = []
    for group in range(len(uCoins)):
        for nCoins in range(1, len(uCoins[group])): # for each possible number of coins to group
        # nComb is in the form [(1, 2), (1, 5), ..., (50, 100)] for nCoins = 2, for example
            nComb = list(combinations(uCoins[group][:-1], nCoins))

            for i in range(len(nComb)): # for each possible group of coins (pCoins)
                test = checkSum(nComb[i], uCoins[group][-1])
                if test[0]:
                    result.append(list(test[1]))
                    result[-1].append(test[2])
    return result

temp = checkComb([[1, 2, 5, 10, 20, 50, 100, 200, 200]])
count = 0
for i in range(200):
    for j in temp:
        if j[-1] == 0:
            count += 1
    temp = checkComb(temp)
    
print(temp)
print(count)