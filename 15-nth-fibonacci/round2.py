def fib(fib_to_find):
    if fib_to_find == 0: return 0

    previous_number = 1
    previous_previous_number = 0

    for index in range(1, fib_to_find):
        temp = previous_number
        previous_number = previous_previous_number + previous_number
        previous_previous_number = temp

    return previous_number