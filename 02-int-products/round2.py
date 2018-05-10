def get_products_of_all_ints_except_at_index(numbers):
    numberOfNumbers = len(numbers)
    if (numberOfNumbers < 3): raise Exception("Must have at least 3 numbers")
    products = [None] * numberOfNumbers

    rollingProduct = 1
    for index in range(0, numberOfNumbers):
        products[index] = rollingProduct
        rollingProduct = numbers[index] * rollingProduct
        print('index: ' + str(index) + '   rolling product:' + str(rollingProduct) + '   before:' + str(products[index]))

    rollingProduct = 1
    for index in range(numberOfNumbers-1, -1, -1):
        products[index] = products[index] * rollingProduct
        rollingProduct = rollingProduct * numbers[index]
        print('index: ' + str(index) + '   rolling product:' + str(rollingProduct) + '   after:' + str(products[index]))

    return products