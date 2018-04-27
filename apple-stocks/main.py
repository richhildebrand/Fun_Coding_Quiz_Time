def get_max_profit(arrayOfPrices):
    min = arrayOfPrices[0]
    max = min

    length = len(arrayOfPrices)
    for index in range(1, length):
        item = arrayOfPrices[index]
        if (item > max): max = item
        if (item < min): min = item

    return max - min