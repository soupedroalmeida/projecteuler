def getRightSum(power):
    result = []
    tempNum = 1
    while True:
        if len(str(tempNum)) > power + 1: break
        tempSum = 0
        for d in str(tempNum): tempSum += int(d) ** power
        if tempSum == tempNum: result.append(tempNum)
        tempNum += 1
    return result

print(sum(getRightSum(5)) - 1)
            

        
            

