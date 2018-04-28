def get_products_of_all_ints_except_at_index(arrayOfInts):
    products = []

    numberOfInts = len(arrayOfInts)
    for outsideIndex in range(0, numberOfInts):
        products.append(1)
        for insideIndex in range(0, numberOfInts):
            if insideIndex != outsideIndex:
                products[outsideIndex] = products[outsideIndex] * arrayOfInts[insideIndex]

    return products
