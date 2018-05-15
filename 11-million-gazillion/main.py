class Crawler(object):

    def __init__(self):
        self.visited = {}

    def addSite(self, site):
        self.visited[site] = site