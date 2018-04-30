def calculateHighestProduct(numbers):
    numberOfNumbers = len(numbers)
    if numberOfNumbers < 2: raise Exception('must have two numbers to multiply!')

    highestNumber = max(numbers[0], numbers[1])
    lowestNumber = min(numbers[0], numbers[1])

    highestProdcutOfThree = numbers[0] * numbers[1]
    highestProductOfTwo = highestProdcutOfThree
    lowestProductOfTwo = highestProdcutOfThree

    for index in range(2, numberOfNumbers):
        number = numbers[index]
        newMaxThree = highestProductOfTwo * number
        newLowThree = lowestProductOfTwo * number
        print()
        print('highest product of three is ' + str(highestProdcutOfThree) + ' for ' + str(index))
        highestProdcutOfThree = max(highestProdcutOfThree, newMaxThree, newLowThree)
        print('highest product of three is ' + str(highestProdcutOfThree) + ' for ' + str(index))

        newMaxTwo = highestNumber * number
        newLowTwo = lowestNumber * number
        highestProductOfTwo = max(highestProductOfTwo, newMaxTwo, newLowTwo)
        lowestProductOfTwo = min(lowestProductOfTwo, newMaxTwo, newLowTwo)

        highestNumber = max(highestNumber, number)
        lowestNumber = min(lowestNumber, number)

    return max(highestProdcutOfThree, highestProductOfTwo)