def getNumberOfSteps(numbers, numberToFind):
    min_index = -1
    max_index = len(numbers)

    steps_taken = 0
    while min_index + 1 < max_index:
        steps_taken += 1
        difference = max_index - min_index
        mid_point = min_index + (difference // 2)

        print('min index: ' + str(min_index) + '   max index: ' + str(max_index) + '   mid point: ' + str(mid_point))
        value = numbers[mid_point]
        if value == numberToFind: return steps_taken
        elif numberToFind < value: max_index = mid_point
        elif numberToFind > value: min_index = mid_point

    return steps_taken
