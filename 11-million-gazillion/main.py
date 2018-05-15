class Crawler(object):

    def __init__(self):
        self.visited = {}

    def addSite(self, site):
        nestedDictionaries = self.visited
        for character in site:
            nestedDictionaries[character] = nestedDictionaries.get(character, {})
            nestedDictionaries = nestedDictionaries[character]

        nestedDictionaries['*'] = True

    def hasSite(self, site):
        try: 
            nestedDictionaries = self.visited
            for character in site:
                nestedDictionaries = nestedDictionaries[character]

            if nestedDictionaries['*']: return True

        except: return False