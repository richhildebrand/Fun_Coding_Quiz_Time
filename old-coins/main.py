def numberOfCombos(amount, denominations):
    numberOfMonies = len(denominations)
    if numberOfMonies == 0: return 0
    if numberOfMonies == 1: 
        if amount % denominations[0] == 0: return 1
        else: return 0

    numberOfCombinationsFor = {}
    numberOfCombinationsFor[0] = 1

    for coinValue in denominations:
        for amountToCheck in range(coinValue, amount + 1):
            difference = amountToCheck - coinValue
            print()
            print('coin:' + str(coinValue) + '   difference:' + str(difference) + '   amountToCheck:' + str(amountToCheck))
            numberOfCombinationsForDifference = numberOfCombinationsFor.get(difference, 0)
            numberOfCombinationsForCurrentAmount = numberOfCombinationsFor.get(amountToCheck, 0)
            numberOfCombinationsFor[amountToCheck] = numberOfCombinationsForDifference + numberOfCombinationsForCurrentAmount
            print('number of combinations for ' + str(amountToCheck) + ' is '+ str(numberOfCombinationsFor[amountToCheck]))

    return numberOfCombinationsFor[amount]