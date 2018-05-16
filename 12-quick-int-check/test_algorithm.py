import unittest
import main


class AlgorithmShould(unittest.TestCase):
    def test_notFindNumber(self):
        numbers = [1, 5, 10, 17, 20]
        numberOfSteps = main.getNumberOfSteps(numbers, 7)
        self.assertEqual(numberOfSteps, -1)

    def test_smoke(self):
        numbers = [1, 5, 10, 17, 20]
        numberOfSteps = main.getNumberOfSteps(numbers, 7)
        self.assertEqual(numberOfSteps, 1)

    def test_findFirstNumber(self):
        numbers = [1, 5, 10, 17, 20]
        numberOfSteps = main.getNumberOfSteps(numbers, 1)
        self.assertEqual(numberOfSteps, 2)

    def test_findLastNumber(self):
        numbers = [1, 5, 10, 17, 20]
        numberOfSteps = main.getNumberOfSteps(numbers, 20)
        self.assertEqual(numberOfSteps, 3)

if __name__ == '__main__':
    unittest.main(verbosity=2)