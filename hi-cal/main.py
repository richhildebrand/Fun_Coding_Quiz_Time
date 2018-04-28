def merge_ranges(meetings):
    numberOfMeetings = len(meetings)

    busyDuring = []
    busyDuring.append(meetings[0])

    for outerIndex in range(1, numberOfMeetings):
        outerStartTime = meetings[outerIndex][0]
        outerEndTime = meetings[outerIndex][1]

        didMerge = False
        numberOfBusyTimeSlots = len(busyDuring)
        for innerIndex in range(0, numberOfBusyTimeSlots):
            innerStartTime = busyDuring[innerIndex][0]
            innerEndTime = busyDuring[innerIndex][1]

            canBeMerged = False
            if outerStartTime <= innerStartTime <= outerEndTime: canBeMerged = True
            if innerStartTime <= outerStartTime <= innerEndTime: canBeMerged = True

            if (canBeMerged):
                newMin = min(innerStartTime, outerStartTime)
                newMax = max(innerEndTime, outerEndTime)

                newTupple = (newMin, newMax)
                busyDuring[innerIndex] = newTupple
                didMerge = True
                break

        if not didMerge: busyDuring.append(meetings[outerIndex])
    
    return busyDuring