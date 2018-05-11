import sys

class TempTracker():
    maxTemp = -sys.maxsize-1
    minTemp = -sys.maxsize

    meanTemp = None
    modeTemp = None

    def insert(newTemp):
        maxTemp = max(newTemp, maxTemp)
        minTemp = min(newTemp, minTemp)

    def get_max():
        return maxTemp

    def get_min()
        return minTemp

    def get_mean()
        return meanTemp

    def get_mode()
        return modeTemp