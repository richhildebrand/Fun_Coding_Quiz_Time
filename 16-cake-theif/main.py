def max_duffel_bag_value(cake_tuples, capacity):

    cake_tuples =   sorted(cake_tuples, key=lambda i: i[0]/i[1])
    print(cake_tuples)

    profit = 0
    cake_tuples_index = 0
    filled_capacity = 0
    while(filled_capacity < capacity):
        weight_of_cake, value_of_cake = cake_tuples[cake_tuples_index]

        cakes_to_put_in_bag = (capacity - filled_capacity) // weight_of_cake
        profit += cakes_to_put_in_bag * value_of_cake
        filled_capacity += cakes_to_put_in_bag * weight_of_cake

        cake_tuples_index += 1

    return profit