def calculateHighestProduct(numbers):
    numberOfNumbers = len(numbers)
    if numberOfNumbers < 3: raise("Must provide at least three numbers")

    highest = max(numbers[0], numbers[1])
    lowest = min(numbers[0], numbers[1])

    highestProductOf3 = numbers[0] * numbers[1]
    highestProductOf2 = highestProductOf3
    lowestProductOf2 = highestProductOf3

    for index in range(2, numberOfNumbers):
        newNumber = numbers[index]

        newHighest3 = highestProductOf2 * newNumber
        highestProductOf3 = max(newHighest3, highestProductOf3)

        newLowest3 = lowestProductOf2 * newNumber
        highestProductOf3 = max(newLowest3, highestProductOf3)

        newHighest2 = max(newNumber*lowest, newNumber*highest)
        highestProductOf2 = max(newHighest2, highestProductOf2)

        newLowest2 = min(newNumber*lowest, newNumber*highest)
        lowestProductOf2 = min(newLowest2, lowestProductOf2)

        lowest = min(newNumber, lowest)
        highest = max(newNumber, highest)

    return max(highestProductOf2, highestProductOf3)