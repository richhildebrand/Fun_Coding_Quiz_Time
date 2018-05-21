import unittest
import main


class AlgorithmShould(unittest.TestCase):
    def test_get_0th(self):
        result = main.fib(0)
        self.assertEqual(result, 0)

    def test_1st(self):
        result = main.fib(1)
        self.assertEqual(result, 1)

    def test_get_2nd(self):
        result = main.fib(2)
        self.assertEqual(result, 1)

    def test_get_3rd(self):
        result = main.fib(3)
        self.assertEqual(result, 2)

    def test_get_4th(self):
        result = main.fib(4)
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main(verbosity=2)