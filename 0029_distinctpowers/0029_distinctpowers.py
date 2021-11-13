def distinctPowers(lowerLimit, upperLimit):
    distinctDict = {}
    for a in range(lowerLimit, upperLimit + 1):
        for b in range(lowerLimit, upperLimit + 1):
            distinctDict[a ** b] = None
    return len(distinctDict)

print(distinctPowers(2, 100))