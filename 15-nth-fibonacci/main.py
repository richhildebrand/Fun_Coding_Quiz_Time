def fib(n):
    if n == 0: return 0
    
    previousPreviousSum = 0
    previousSum = 1
    for number in range(2, n):
        temp = previousSum
        previousSum = previousSum + previousPreviousSum
        previousPreviousSum = temp

    return previousPreviousSum + previousSum