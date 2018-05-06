import unittest
import main as main


class AlgorithmShould(unittest.TestCase):
    def test_withOneMode(self):
        tempTracker = main.TempTracker()
        tempTracker.insert(10)
        tempTracker.insert(10)
        tempTracker.insert(5)
        tempTracker.insert(15)

        self.assertEqual(tempTracker.get_max(), 15)
        self.assertEqual(tempTracker.get_min(), 5)
        self.assertEqual(tempTracker.get_mean(), 10)
        self.assertEqual(tempTracker.get_mode(), [10])

    def test_withThreeModes(self):
        tempTracker = main.TempTracker()
        tempTracker.insert(10)
        tempTracker.insert(20)
        tempTracker.insert(30)
        tempTracker.insert(30)
        tempTracker.insert(20)
        tempTracker.insert(10)

        self.assertEqual(tempTracker.get_max(), 30)
        self.assertEqual(tempTracker.get_min(), 10)
        self.assertEqual(tempTracker.get_mean(), 20)
        self.assertEqual(tempTracker.get_mode(), [30, 20, 10])


if __name__ == '__main__':
    unittest.main(verbosity=2)