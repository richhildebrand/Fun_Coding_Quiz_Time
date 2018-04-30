import unittest as unittest
import round2 as main


class HighestProductShould(unittest.TestCase):
    def test_returnProductOfThreeNumbers(self):
        input = [1, 2, 3]
        product = main.calculateHighestProduct(input)
        self.assertEquals(product, 6)

    def test_workWithTwoNegativeNumbers(self):
        input = [1, 10, -5, 1, -100]
        product = main.calculateHighestProduct(input)
        self.assertEquals(product, 5000)

    def test_workWithFiveNumbers(self):
        input = [5, 3, 10, 2, 1]
        product = main.calculateHighestProduct(input)
        self.assertEquals(product, 150)

    def test_firstNumberIsZero(self):
        input = [0, 3, 10]
        product = main.calculateHighestProduct(input)
        self.assertEquals(product, 30)

    def test_secondNumberIsZero(self):
        input = [5, 0, 10]
        product = main.calculateHighestProduct(input)
        self.assertEquals(product, 50)

    def test_lastNumberIsZero(self):
        input = [5, 1, 0]
        product = main.calculateHighestProduct(input)
        self.assertEquals(product, 5)

    def test_throwWithLessThanTwo(self):
        input = [5]
        with self.assertRaises(Exception): main.calculateHighestProduct(input)


if __name__ == '__main__':
    unittest.main(verbosity=2)