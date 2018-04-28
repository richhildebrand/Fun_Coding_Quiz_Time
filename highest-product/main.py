def calculateHighestProduct(numbers):
    numberOfNumbers = len(numbers)
    product = 1

    for index in range(0, numberOfNumbers):
        product *= numbers[index]

    return product