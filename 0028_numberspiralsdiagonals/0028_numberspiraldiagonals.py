from math import sqrt

def sumDiagonals(maxRange):
    lastSquares = [1]
    result = 1
    while lastSquares[-1] < maxRange ** 2:
        lastSquares.append((sqrt(lastSquares[-1]) + 2) ** 2)
        print(lastSquares)
    for i in lastSquares:
        temp = i
        for c in range(4):
            if i > 1: 
                result += temp
                temp -= sqrt(i) - 1
    return result

print(sumDiagonals(1001))