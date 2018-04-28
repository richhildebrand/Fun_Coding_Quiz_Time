import sys
sys.path.append('../testHelpers')
import testHelpers.assertHelpers as assertHelpers
import unittest as unittest
import main as main


class IntProductsShould(unittest.TestCase):

    def test_sequenceEqual_with_same_arry(self):
        result = [84, 12, 28, 21]
        assert assertHelpers.sequenceEqual(result, result)

    def test_sequenceEqual_with_different_sequence(self):
        isTrue = main.returnTrue()
        assert isTrue

if __name__ == '__main__':
    unittest.main()