import unittest
import main


class AlgorithmShould(unittest.TestCase):
    def test_storeGoogle(self):
        crawler = main.Crawler()
        crawler.addSite('www.google.com')

        expected = { 'www.': { 'google.com': None } }
        self.assertDictEqual(expected, crawler.visited)


if __name__ == '__main__':
    unittest.main(verbosity=2)