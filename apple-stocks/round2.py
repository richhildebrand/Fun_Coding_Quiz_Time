def get_max_profit(stockPrices):
    numberOfPrices = len(stockPrices)
    if numberOfPrices == 0: return 0 #we did not buy or sell
    if numberOfPrices == 1: return -stockPrices[0] #we bought but could not sell

    minPrice = min(stockPrices[0], stockPrices[1])
    largestProfit = stockPrices[1] - stockPrices[0]

    for index in range(2, numberOfPrices):
        newProfitPotential = stockPrices[index] - minPrice
        largestProfit = max(largestProfit, newProfitPotential)
        minPrice = min(minPrice, stockPrices[index])

    return largestProfit