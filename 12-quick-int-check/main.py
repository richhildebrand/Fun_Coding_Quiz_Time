def getNumberOfSteps(numbers, numberToFind):
    maxIndex = len(numbers)
    minIndex = 0

    stepCount = 0
    while maxIndex != minIndex:
        print('maxIndex:' + str(maxIndex) + '   minIndex:' + str(minIndex))
        stepCount += 1
        midPoint = (minIndex + maxIndex) // 2
        print('midPoint:' + str(midPoint))
        numberToCheck = numbers[midPoint]
        print('numberToCheck:' + str(numberToCheck))

        if numberToCheck == numberToFind: return stepCount
        elif numberToFind > numberToCheck: minIndex = midPoint
        elif numberToFind < numberToCheck: maxIndex = midPoint 


    return -1