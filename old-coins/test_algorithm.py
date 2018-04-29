import unittest
import main


class AlgorithmShould(unittest.TestCase):
    def test_givenExample(self):
        denominations = [1,2,3]
        result = main.numberOfCombos(44, denominations)
        self.assertEqual(result, 44)


if __name__ == '__main__':
    unittest.main(verbosity=2)