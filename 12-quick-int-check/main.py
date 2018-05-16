def getNumberOfSteps(numbers, numberToFind):
    maxIndex = len(numbers)
    minIndex = -1

    stepCount = 0
    while minIndex + 1 < maxIndex:
        stepCount += 1
        print('maxIndex:' + str(maxIndex) + '   minIndex:' + str(minIndex))
        
        distance = maxIndex - minIndex
        halfDistance = distance // 2
        midPoint = halfDistance + minIndex
        numberToCheck = numbers[midPoint]
        print('midPoint:' + str(midPoint))
        print('numberToCheck:' + str(numberToCheck))

        if numberToCheck == numberToFind: return stepCount
        elif numberToFind > numberToCheck: minIndex = midPoint
        elif numberToFind < numberToCheck: maxIndex = midPoint 


    return stepCount