import statistics
import sys

class TempTracker():

    def __init__(self):
        self.minTemp = sys.maxsize
        self.maxTemp = -sys.maxsize -1
        self.meanOfTemps = None
        self.modeOfTemps = None
        self.allTemps = []

    def insert(self, newTemp):
        self.minTemp = min(self.minTemp, newTemp)
        self.maxTemp = max(self.maxTemp, newTemp)

        self.allTemps.append(newTemp)
        self.meanOfTemps = statistics.mean(self.allTemps)
        self.modeOfTemps = statistics.mode(self.allTemps)


    def get_max(self):
        return self.maxTemp

    def get_min(self):
        return self.minTemp

    def get_mean(self):
        return self.meanOfTemps

    def get_mode(self):
        return self.modeOfTemps
    
