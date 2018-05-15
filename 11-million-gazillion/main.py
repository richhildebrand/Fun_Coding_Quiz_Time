class Crawler(object):

    def __init__(self):
        self.visited = {}
        self.visited['www.'] = {}

    def addSite(self, site):
        if self.isWWWSite(site): 
            site = self.trimWWW(site)
            self.visited['www.'][site] = None
        else:
            self.visited[site] = None



    def isWWWSite(self, site):
        return site.startswith('www.')

    def trimWWW(self, site):
        return site[4:]