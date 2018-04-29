import unittest
import main


class AlgorithmShould(unittest.TestCase):
    def test_givenThreeCoins(self):
        denominations = [1, 2, 3]
        result = main.numberOfCombos(4, denominations)
        self.assertEqual(result, 4)

    def test_givenTwoCoins(self):
        denominations = [1, 2]
        result = main.numberOfCombos(10, denominations)
        self.assertEqual(result, 6)

    def test_givenOneCoin_ThatWorks(self):
        denominations = [1]
        result = main.numberOfCombos(7, denominations)
        self.assertEqual(result, 1)

    def test_givenOneCoin_ThatDoesNotWork(self):
        denominations = [10]
        result = main.numberOfCombos(5, denominations)
        self.assertEqual(result, 0)

    def test_givenZeroCoins(self):
        denominations = []
        result = main.numberOfCombos(5, denominations)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)