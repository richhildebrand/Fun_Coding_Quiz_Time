def max_duffel_bag_value(cake_tuples, capacity):

    profits = {}
    profits[0] = 0
 
    for current_capacity in range(0, capacity+1):
        max_profit_at_current_capacity = 0

        for weight, value in cake_tuples:
            if weight > current_capacity: continue
            if weight == 0 and value > 0: return float('inf')

            profit_with_cake = value + profits[current_capacity - weight]
            max_profit_at_current_capacity = max(max_profit_at_current_capacity, profit_with_cake)


        print('capacity:' + str(current_capacity) + '   max to add:' + str(max_profit_at_current_capacity))
        profits[current_capacity] = max_profit_at_current_capacity
    

    return profits[capacity]