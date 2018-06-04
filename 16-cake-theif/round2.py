def max_duffel_bag_value(cake_tuples, capacity):
    max_profits = {}

    for current_capacity in range(0, capacity+1):
        max_profits[current_capacity] = max_profits.get(current_capacity, 0)

        for weight, value in cake_tuples:
            if weight > current_capacity: continue

            remainder = current_capacity - weight
            potential_profit = value + max_profits[remainder]
            max_profit = max_profits[current_capacity]

            if potential_profit > max_profit: max_profits[current_capacity] = potential_profit


    return max_profits[capacity]