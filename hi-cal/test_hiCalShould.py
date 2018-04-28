import unittest
import main


class HiCalShould(unittest.TestCase):
    def test_mergeTwoRanges(self):
        meetings = [(1, 3), (2, 4)]
        
        result = main.merge_ranges(meetings)
        
        expectedResult = [(1, 4)]
        self.assertSequenceEqual(result, expectedResult)

    def test_keepTwoRanges(self):
        meetings = [(1, 3), (7, 10)]
        
        result = main.merge_ranges(meetings)
        
        expectedResult = [(1, 3), (7, 10)]
        self.assertSequenceEqual(result, expectedResult)

    def test_mergeRanges_InOrder(self):
        meetings = [(0, 1), (3, 5), (4, 8), (9, 10), (10, 12)]
        
        result = main.merge_ranges(meetings)
        
        expectedResult = [(0, 1), (3, 8), (9, 12)]
        self.assertSequenceEqual(result, expectedResult)

    def test_mergeRanges_OutOfOrder(self):
        meetings = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
        
        result = main.merge_ranges(meetings)
        
        expectedResult = [(0, 1), (3, 8), (9, 12)]
        self.assertSequenceEqual(result, expectedResult)


if __name__ == '__main__':
    unittest.main(verbosity=2)