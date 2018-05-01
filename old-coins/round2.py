def numberOfCombos(totalAmount, denominations):
    numberOfDenominations = len(denominations)
    if numberOfDenominations == 0: return 0
    if numberOfDenominations == 1: return (totalAmount % denominations[0]) == 0

    numberOfCombosFor = {}
    numberOfCombosFor[0] = 1

    for coinValue in denominations:
        for incrementalAmount in range(coinValue, totalAmount+1):
            difference = incrementalAmount - coinValue
            numberOfCombosFor[incrementalAmount] = numberOfCombosFor.get(incrementalAmount, 0) + numberOfCombosFor.get(difference, 0)

    return numberOfCombosFor[totalAmount]