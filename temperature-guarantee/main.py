import statistics
import sys

class TempTracker():

    def __init__(self):
        self.minTemp = sys.maxsize
        self.maxTemp = -sys.maxsize -1
        self.meanOfTemps = None
        self.modeOfTemps = []

        self.numberOfTemps = 0
        self.sumOfTemps = 0
        self.maxOccurancesOfTemp = 0
        self.allTemps = {}

    def insert(self, newTemp):
        self.minTemp = min(self.minTemp, newTemp)
        self.maxTemp = max(self.maxTemp, newTemp)

        self.numberOfTemps += 1
        self.sumOfTemps += newTemp
        self.meanOfTemps = self.sumOfTemps / self.numberOfTemps

        newTempCount = self.allTemps[newTemp] = self.allTemps.get(newTemp, 0) + 1
        print('new temp count:' + str(newTempCount), '   new temp:' + str(newTemp))
        
        if newTempCount > self.maxOccurancesOfTemp:
            self.modeOfTemps = [newTemp]
            self.maxOccurancesOfTemp = newTempCount
        elif newTempCount == self.maxOccurancesOfTemp:
            self.modeOfTemps.append(newTemp) 



    def get_max(self):
        return self.maxTemp

    def get_min(self):
        return self.minTemp

    def get_mean(self):
        return self.meanOfTemps

    def get_mode(self):
        return self.modeOfTemps
    
