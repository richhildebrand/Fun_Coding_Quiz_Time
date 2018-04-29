def numberOfCombos(amount, denominations):
    numberOfMonies = len(denominations)
    if numberOfMonies == 0: return 0
    if numberOfMonies == 1: 
        if amount % denominations[0] == 0: return 1
        else: return 0

    return 0