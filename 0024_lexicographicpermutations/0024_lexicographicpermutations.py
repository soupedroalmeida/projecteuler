from math import factorial

def getNumber(position, numbers):
    def chooseBranch(initial, position):
        branch = 0
        for i in list(range(initial)):
            if position <= (i + 1) * factorial(initial - 1): break
            branch = i + 1
        return branch
    
    tempPos = position
    tempInitial = len(numbers)
    coordinates = []
    while len(coordinates) < len(numbers) - 1:
        coordinates.append(chooseBranch(tempInitial, tempPos))
        tempPos -= coordinates[-1] * factorial(tempInitial - 1)
        tempInitial -= 1
    
    tempNumbers = numbers
    result = ''
    for i in coordinates:
        result += str(tempNumbers[i])
        tempNumbers.pop(i)
    result += str(tempNumbers[0])

    return result

print(getNumber(1000000, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))