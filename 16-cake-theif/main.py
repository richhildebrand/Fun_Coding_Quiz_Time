def max_duffel_bag_value(cake_tuples, capacity):

    profits = {}
    profits[0] = 0
 
    for current_capacity in range(1, capacity+1):
        max_profit_at_current_capacity = 0

        for weight, value in cake_tuples:
            if weight > current_capacity: continue

            remainder = current_capacity % weight
            number_of_possible_cakes = current_capacity // weight
            profit_from_cake = number_of_possible_cakes * value

            total_profit_with_cake = profit_from_cake + profits[remainder]
            print('new profit:' + str(total_profit_with_cake) + '   current max:' + str(max_profit_at_current_capacity))
            if total_profit_with_cake > max_profit_at_current_capacity:
                max_profit_at_current_capacity = total_profit_with_cake


        print('capacity:' + str(current_capacity) + '   max to add:' + str(max_profit_at_current_capacity))
        profits[current_capacity] = max_profit_at_current_capacity
    

    return profits[capacity]