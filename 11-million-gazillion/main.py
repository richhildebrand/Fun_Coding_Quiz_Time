class Crawler(object):

    def __init__(self):
        self.visited = {}

    def addSite(self, site):
        nestedDictionaries = self.visited
        for character in site:
            nestedDictionaries[character] = nestedDictionaries.get(character, {})
            nestedDictionaries = nestedDictionaries[character]

    def trimWWW(self, site):
        return site[4:]