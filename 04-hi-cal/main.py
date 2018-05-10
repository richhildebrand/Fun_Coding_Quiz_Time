def merge_ranges(meetings):
    numberOfMeetings = len(meetings)
    meetings = sorted(meetings) #costs O(n lg n)

    busyDuring = []
    busyDuring.append(meetings[0])
    for index in range(0, numberOfMeetings-1): #costs O(n)
        currentStartTime = meetings[index][0]
        currentEndTime = meetings[index][1]

        nextIndex = index + 1
        nextStartTime = meetings[nextIndex][0]
        nextEndTime = meetings[nextIndex][1]

        canBeMerged = False
        if currentStartTime <= nextStartTime <= currentEndTime: canBeMerged = True
        if nextStartTime <= currentEndTime <= nextEndTime: canBeMerged = True

        if (canBeMerged):
            newMin = min(currentStartTime, nextStartTime)
            newMax = max(currentEndTime, nextEndTime)

            newTupple = (newMin, newMax)
            lastIndex = len(busyDuring) - 1
            busyDuring[lastIndex] = newTupple
        else:
            busyDuring.append(meetings[nextIndex])
    
    return busyDuring