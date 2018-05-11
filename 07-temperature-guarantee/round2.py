import sys

class TempTracker():
    maxTemp = -sys.maxsize-1
    minTemp = -sys.maxsize

    sumOfTemps = 0
    numberOfTemps = 0
    meanTemp = None

    modeTemp = None

    def insert(self, newTemp):
        self.maxTemp = max(newTemp, self.maxTemp)
        self.minTemp = min(newTemp, self.minTemp)

        self.sumOfTemps += newTemp
        self.numberOfTemps += 1
        self.meanTemp = self.sumOfTemps / self.numberOfTemps



    def get_max(self):
        return self.maxTemp

    def get_min(self):
        return self.minTemp

    def get_mean(self):
        return self.meanTemp

    def get_mode(self):
        return self.modeTemp
