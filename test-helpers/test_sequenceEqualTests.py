import unittest as unittest
import testHelpers as testHelpers

class SequenceEqualShould(unittest.TestCase):

    def test_sequenceEqual_with_same_arry(self):
        result = [84, 12, 28, 21]
        assert testHelpers.sequenceEqual(result, result)

    def test_sequenceEqual_with_different_sequence(self):
        result = [84, 12, 28, 21]
        differentResult = [12, 84, 28, 21]
        
        areEqual = testHelpers.sequenceEqual(result, differentResult)
        
        assert areEqual is False

    def test_sequenceEqual_with_different_length(self):
        result = [84, 12, 28, 21]
        differentResult = [84, 12, 28, 21, 55]
        
        areEqual = testHelpers.sequenceEqual(result, differentResult)
        
        assert areEqual is False

if __name__ == '__main__':
    unittest.main()