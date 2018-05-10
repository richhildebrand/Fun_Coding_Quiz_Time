def merge_ranges(meetings):
    numberOfMeetings = len(meetings)
    meetings = sorted(meetings)

    combinedMeetings = []
    combinedMeetings.append(meetings[0])
    for currentIndex in range(0, numberOfMeetings-1):
        currentStartTime = meetings[currentIndex][0]
        currentEndTime = meetings[currentIndex][1]

        nextIndex = currentIndex + 1
        nextStartTime = meetings[nextIndex][0]
        nextEndTime = meetings[nextIndex][1]

        hasOverlap = False
        if (currentStartTime <= nextStartTime <= currentEndTime): hasOverlap = True
        if (currentStartTime <= nextEndTime <= currentEndTime): hasOverlap = True

        if hasOverlap: 
            indexToOverlap = len(combinedMeetings) - 1
            newStartTime = min(currentStartTime, nextStartTime)
            newEndTime = max(currentEndTime, nextEndTime)
            combinedMeetings[indexToOverlap] = (newStartTime, newEndTime)
        else:
            combinedMeetings.append(meetings[nextIndex])

    return combinedMeetings
