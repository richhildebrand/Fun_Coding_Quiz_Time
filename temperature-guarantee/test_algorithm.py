import unittest
import main as main


class AlgorithmShould(unittest.TestCase):
    def test_withFour_easyNumbers(self):
        tempTracker = main.TempTracker()
        tempTracker.insert(10)
        tempTracker.insert(10)
        tempTracker.insert(5)
        tempTracker.insert(15)

        self.assertEqual(tempTracker.get_max(), 15)
        self.assertEqual(tempTracker.get_min(), 5)
        self.assertEqual(tempTracker.get_mean(), 10)
        self.assertEqual(tempTracker.get_mode(), 10)


if __name__ == '__main__':
    unittest.main(verbosity=2)