def calculateHighestProduct(numbers):
    numberOfNumbers = len(numbers)
    max1 = 0
    max2 = 0
    max3 = 0

    for index in range(0, numberOfNumbers):
        number = numbers[index]
        if number > max3:
            max1 = max2 
            max2 = max3
            max3 = number
        elif number > max2:
            max1 = max2
            max2 = number
        elif number > max1:
            max2 = number

    maxAll = max1 * max2 * max3
    max12 = max1 * max2
    max13 = max1 * max3
    max23 = max2 * max3

    return max(maxAll, max12, max13, max23)