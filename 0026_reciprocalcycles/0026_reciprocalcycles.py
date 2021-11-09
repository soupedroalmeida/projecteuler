def findCycle(d):
    remainders = [10]
    cycle = ''
    tempRemainder = 0
    while True:
        tempRemainder = remainders[-1] % d
        if tempRemainder == 0: return ''
        remainders.append(tempRemainder * 10)
        if tempRemainder * 10 in remainders[:-1]: break
    remainders = remainders[remainders.index(remainders[-1]): -1]
    for r in remainders: cycle += str(r // d)

    return cycle

resCycle = ''
result = None
for i in range(1, 1000):
    if len(findCycle(i)) > len(resCycle): 
        resCycle = findCycle(i)
        result = i
print(result)