import sys as sys

def get_max_profit(arrayOfPrices):
    maxProfit = -sys.maxsize - 1

    currentMin = arrayOfPrices[0]
    length = len(arrayOfPrices)
    for index in range(1, length):
        value = arrayOfPrices[index]

        difference = value - currentMin
        maxProfit = max(maxProfit, difference)
        currentMin = min(currentMin, value)

    return maxProfit