import unittest
import main


class AlgorithmShould(unittest.TestCase):
    def test_storeSite(self):
        crawler = main.Crawler()
        crawler.addSite('123')

        expected = { '1': { '2': { '3': {'*': True } } } }
        self.assertDictEqual(expected, crawler.visited)

    def test_storeManySites(self):
        crawler = main.Crawler()
        crawler.addSite('123')
        crawler.addSite('12345')
        crawler.addSite('abc')
        crawler.addSite('axyz')


        expected = \
        { 
            '1': { '2': { '3':
                            { '*': True,
                            '4': { '5': { '*': True } }
                            }
                        } 
            }, 
            'a': {
                    'b':{ 'c': {'*': True } },
                    'x':{ 'y': {'z': {'*': True } } }
                }
        }
        self.assertDictEqual(expected, crawler.visited)
        self.assertTrue(crawler.hasSite('123'))
        self.assertTrue(crawler.hasSite('12345'))
        self.assertTrue(crawler.hasSite('abc'))
        self.assertTrue(crawler.hasSite('axyz'))

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