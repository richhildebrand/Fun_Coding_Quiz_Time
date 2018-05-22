class Crawler():

    def __init__(self):
        self.visited = {}

    def addSite(self, site):
        currentDictionary = self.visited
        for letter in site:
            currentDictionary[letter] = currentDictionary.get(letter, {})
            currentDictionary = currentDictionary[letter]

        currentDictionary['*'] = True
    
    def hasSite(self, site):
        currentDictionary = self.visited
        for letter in site:
                currentDictionary = currentDictionary.get(letter, False)
                if currentDictionary == False: return False

        return currentDictionary.get('*', False)