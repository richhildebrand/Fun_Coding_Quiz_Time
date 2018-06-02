import unittest
import main


class AlgorithmShould(unittest.TestCase):
    def test_smoke(self):
        queue = main.MyQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        result, steps = queue.dequeue()
        self.assertEqual(result, 1)
        self.assertEqual(steps, 3)


if __name__ == '__main__':
    unittest.main(verbosity=2)