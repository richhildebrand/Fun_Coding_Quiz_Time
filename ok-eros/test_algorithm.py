import unittest
import main


class AlgorithmShould(unittest.TestCase):
    def test_smoke(self):
        result = main.gettingStarted()
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main(verbosity=2)