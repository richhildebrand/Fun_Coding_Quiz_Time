def get_max_profit(arrayOfPrices):
    min = arrayOfPrices[0]
    max = min

    length = len(arrayOfPrices)
    for index in range(1, length):
        item = arrayOfPrices[index]
        if (item > max): max = item
        if (item < min): min = item

    return max - min



stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
result = get_max_profit(stock_prices_yesterday)
print(result)
# Returns 6 (buying for $5 and selling for $11)