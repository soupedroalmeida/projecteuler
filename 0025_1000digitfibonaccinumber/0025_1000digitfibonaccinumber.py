def getFibonacci(index):
    tempIndex = 1
    result = 1
    a = 1
    while tempIndex < index:
        b = a + result
        result = a
        a = b
        tempIndex += 1
    return result

def firstIndex(digits):
    index = 1
    while True:
        digitCount = len(str(getFibonacci(index)))
        if digitCount >= digits: break
        index += 1
    return index

print(firstIndex(1000))