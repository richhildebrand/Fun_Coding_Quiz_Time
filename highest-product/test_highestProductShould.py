import unittest as unittest
import main as main


class HighestProductShould(unittest.TestCase):
    def test_returnProductOfThreeNumbers(self):
        input = [1, 2, 3]
        product = main.calculateHighestProduct(input)
        assert product == 6


if __name__ == '__main__':
    unittest.main(verbosity=2)