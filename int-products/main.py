def get_products_of_all_ints_except_at_index(arrayOfInts):
    numberOfInts = len(arrayOfInts)
    products = [None] * numberOfInts

    rollingProduct = 1
    productsBeforeIndex = [None] * numberOfInts
    for index in range(0, numberOfInts):
        productsBeforeIndex[index] = rollingProduct
        rollingProduct = rollingProduct * arrayOfInts[index]

    rollingProduct = 1
    productsAfterIndex = [None] * numberOfInts
    for index in range(numberOfInts -1, -1, -1):
        productsAfterIndex[index] = rollingProduct
        rollingProduct = rollingProduct * arrayOfInts[index]

    for index in range(0, numberOfInts):
        products[index] = productsBeforeIndex[index] * productsAfterIndex[index]

    return products
