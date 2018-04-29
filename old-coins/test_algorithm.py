import unittest
import main


class AlgorithmShould(unittest.TestCase):
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

    # def test_givenExample(self):
    #     denominations = [1,2,3]
    #     result = main.numberOfCombos(44, denominations)
    #     self.assertEqual(result, 44)


if __name__ == '__main__':
    unittest.main(verbosity=2)