import unittest
import main


class AlgorithmShould(unittest.TestCase):
    def test_storeGoogle(self):
        crawler = main.Crawler()
        crawler.addSite('123')

        expected = { '1': { '2': { '3': {} } } }
        self.assertDictEqual(expected, crawler.visited)


if __name__ == '__main__':
    unittest.main(verbosity=2)