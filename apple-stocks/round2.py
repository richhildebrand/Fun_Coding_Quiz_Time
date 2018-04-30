def get_max_profit(stockPrices):
    numberOfPrices = len(stockPrices)
    if numberOfPrices == 0: return 0 #we did not buy or sell
    if numberOfPrices == 1: return -stockPrices[0] #we bought but could not sell

    minPrice = stockPrices[0]
    largestProfit = stockPrices[1] - stockPrices[0]



    return 0