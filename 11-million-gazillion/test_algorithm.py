import unittest
import round2 as main


class AlgorithmShould(unittest.TestCase):
    def setUp(self):
        self.crawler = main.Crawler()

    def test_storeSite(self):
        self.crawler.addSite('123')
        expected = { '1': { '2': { '3': {'*': True } } } }
        self.assertDictEqual(expected, self.crawler.visited)

    def test_storeManySites(self):
        self.crawler.addSite('123')
        self.crawler.addSite('12345')
        self.crawler.addSite('abc')
        self.crawler.addSite('axyz')


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

        self.assertDictEqual(expected, self.crawler.visited)
        self.assertTrue(self.crawler.hasSite('123'))
        self.assertTrue(self.crawler.hasSite('12345'))
        self.assertTrue(self.crawler.hasSite('abc'))
        self.assertTrue(self.crawler.hasSite('axyz'))

    def test_knowIfVisited(self):
        self.crawler.addSite('123')
        hasVisited = self.crawler.hasSite('123')
        self.assertTrue(hasVisited)

    def test_knowIfNotVisisted_BecauseTooLong(self):
        self.crawler.addSite('123')
        hasVisited = self.crawler.hasSite('1234')
        self.assertFalse(hasVisited)
    
    def test_knowIfNotVisisted_becauseTooShort(self):
        self.crawler.addSite('123')
        hasVisited = self.crawler.hasSite('12')
        self.assertFalse(hasVisited)



if __name__ == '__main__':
    unittest.main(verbosity=2)