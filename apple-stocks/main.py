def get_max_profit(arrayOfPrices):
    maxProfit = 0

    length = len(arrayOfPrices)
    for outerIndex in range(0, length):
        outerValue = arrayOfPrices[outerIndex]
        innerStart = outerIndex + 1

        for innerIndex in range(innerStart , length):
            innerValue = arrayOfPrices[innerIndex]

            difference = innerValue - outerValue
            if (difference > maxProfit): 
                maxProfit = difference

    return maxProfit