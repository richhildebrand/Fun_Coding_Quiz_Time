import unittest
import main


class AlgorithmShould(unittest.TestCase):
    def test_work_with_one_dequeue(self):
        queue = main.MyQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        result, steps = queue.dequeue()

        self.assertEqual(result, 1)
        self.assertEqual(steps, 3)

    def test_work_with_two_dequeues_in_a_row(self):
        queue = main.MyQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        queue.dequeue()
        result, steps = queue.dequeue()

        self.assertEqual(result, 2)
        self.assertEqual(steps, 0)

    def test_work_with_two_dequeues_out_of_order(self):
        queue = main.MyQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        queue.dequeue()
        queue.enqueue(4)
        result, steps = queue.dequeue()

        self.assertEqual(result, 2)
        self.assertEqual(steps, 0)

    def test_work_with_complicated_test(self):
        queue = main.MyQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        queue.dequeue()
        queue.enqueue(4)
        queue.enqueue(5)
        queue.dequeue()
        queue.dequeue()
        result, steps = queue.dequeue()


        self.assertEqual(result, 4)
        self.assertEqual(steps, 2)



if __name__ == '__main__':
    unittest.main(verbosity=2)