def get_products_of_all_ints_except_at_index(arrayOfInts):
    numberOfInts = len(arrayOfInts)
    products = [None] * numberOfInts

    rollingProduct = 1
    productsBeforeIndex = [None] * numberOfInts
    for index in range(0, numberOfInts):
        productsBeforeIndex[index] = rollingProduct
        rollingProduct = rollingProduct * arrayOfInts[index]

    rollingProduct = 1
    products = [None] * numberOfInts
    for index in range(numberOfInts -1, -1, -1):
        products[index] = rollingProduct * productsBeforeIndex[index]
        rollingProduct = rollingProduct * arrayOfInts[index]

    return products
