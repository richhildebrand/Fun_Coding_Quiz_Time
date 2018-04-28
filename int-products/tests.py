import unittest as unittest
import main as main

class OurTests(unittest.TestCase):
    def sequenceEqual(self, a, b):
        if len(a) != len(b): return False
        
        for index in range(0, len(a)):
            if a[index] != b[index]: return False

        return True

    def test_sequenceEqual_with_same_arry(self):
        result = [84, 12, 28, 21]
        assert self.sequenceEqual(result, result)

    def test_sequenceEqual_with_different_sequence(self):
        result = [84, 12, 28, 21]
        differentResult = [12, 84, 28, 21]
        
        areEqual = self.sequenceEqual(result, differentResult)
        
        assert areEqual is False

    def test_sequenceEqual_with_different_length(self):
        result = [84, 12, 28, 21]
        differentResult = [84, 12, 28, 21, 55]
        
        areEqual = self.sequenceEqual(result, differentResult)
        
        assert areEqual is False

if __name__ == '__main__':
    unittest.main()