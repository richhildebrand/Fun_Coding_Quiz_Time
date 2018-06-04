def max_duffel_bag_value(cake_tuples, capacity):
    max_profits = {}

    for current_capacity in range(1, capacity+1):

        for weight, value in cake_tuples:
            if weight > current_capacity: continue

            remainder = current_capacity - weight
            potential_profit = value + max_profits[remainder]
            max_profit = current_capacity.get(current_capacity, 0)

            if potential_profit > max_profit: max_profits[current_capacity] = max_profit


    return max_profits[capacity]