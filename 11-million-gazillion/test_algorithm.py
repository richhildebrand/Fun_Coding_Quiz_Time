import unittest
import main


class AlgorithmShould(unittest.TestCase):
    def test_storeGoogle(self):
        crawler = main.Crawler()
        crawler.addSite('123')

        expected = { '1': { '2': { '3': {'*'} } } }
        self.assertDictEqual(expected, crawler.visited)

    def test_knowIfVisited(self):
        crawler = main.Crawler()
        crawler.addSite('123')

        hasVisited = crawler.hasSite('123')
        self.assertTrue(hasVisited)

    def test_knowIfNotVisisted_BecauseTooLong(self):
        crawler = main.Crawler()
        crawler.addSite('123')
        
        hasVisited = crawler.hasSite('1234')
        self.assertFalse(hasVisited)
    
    def test_knowIfNotVisisted_becauseTooShort(self):
        crawler = main.Crawler()
        crawler.addSite('123')

        hasVisited = crawler.hasSite('12')
        self.assertFalse(hasVisited)



if __name__ == '__main__':
    unittest.main(verbosity=2)