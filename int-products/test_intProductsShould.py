import unittest as unittest
import round2 as main


class IntProductsShould(unittest.TestCase):
    def test_returnProducts(self):
        input = [1, 7, 3, 4]
        output = main.get_products_of_all_ints_except_at_index(input)

        expectedOutput = [84, 12, 28, 21]
        self.assertSequenceEqual(output, expectedOutput)

    def test_allowZeros(self):
        input = [1, 0, 3, 4]
        output = main.get_products_of_all_ints_except_at_index(input)

        expectedOutput = [0, 12, 0, 0]
        self.assertSequenceEqual(output, expectedOutput)


if __name__ == '__main__':
    unittest.main()