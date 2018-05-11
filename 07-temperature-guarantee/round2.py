import sys

class TempTracker():
    def __init__(self):
        self.maxTemp = -sys.maxsize-1
        self.minTemp = sys.maxsize

        self.sumOfTemps = 0
        self.numberOfTemps = 0
        self.meanTemp = None

        self.maxTempOccurances = 0
        self.seenTemps = {}
        self.modeTemp = None

    def insert(self, newTemp):
        self.maxTemp = max(newTemp, self.maxTemp)
        self.minTemp = min(newTemp, self.minTemp)

        self.sumOfTemps += newTemp
        self.numberOfTemps += 1
        self.meanTemp = self.sumOfTemps / self.numberOfTemps

        newTempCount = self.seenTemps[newTemp] = self.seenTemps.get(newTemp, 0) + 1
        print('newTemp:' + str(newTemp) + '   newTempCount:'+ str(newTempCount) + '   maxTempOccurances:'+ str(self.maxTempOccurances))
        if newTempCount > self.maxTempOccurances:
            self.modeTemp = [newTemp]
            self.maxTempOccurances = newTempCount   
        elif newTempCount == self.maxTempOccurances:
            self.modeTemp.append(newTemp)


    def get_max(self):
        return self.maxTemp

    def get_min(self):
        return self.minTemp

    def get_mean(self):
        return self.meanTemp

    def get_mode(self):
        return self.modeTemp
