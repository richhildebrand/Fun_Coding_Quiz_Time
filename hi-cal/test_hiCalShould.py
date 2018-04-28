import unittest
import main


class HiCalShould(unittest.TestCase):
    def test_mergeRanges(self):
        meetings = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
        
        result = main.merge_ranges(meetings)
        
        expectedResult = [(0, 1), (3, 8), (9, 12)]
        self.assertSequenceEqual(result, expectedResult)


if __name__ == '__main__':
    unittest.main(verbosity=2)