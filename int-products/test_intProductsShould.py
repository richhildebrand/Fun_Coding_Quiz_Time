import sys
sys.path.append('../testHelpers')
import testHelpers.assertHelpers as assertHelpers
import unittest as unittest
import main as main


class IntProductsShould(unittest.TestCase):
    def test_returnProducts(self):
        input = [1, 7, 3, 4]
        output = main.get_products_of_all_ints_except_at_index(input)

        expectedOutput = [84, 12, 28, 21]
        assert assertHelpers.sequenceEqual(output, expectedOutput)

if __name__ == '__main__':
    unittest.main()