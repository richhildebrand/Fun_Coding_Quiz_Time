import unittest
import main


class AlgorithmShould(unittest.TestCase):
    def test_smoke(self):
        result = main.gettingStarted()
        self.assertTrue(result)



class Stack(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push new item to stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """See what the last item is"""
        if not self.items:
            return None
        return self.items[-1]


if __name__ == '__main__':
    unittest.main(verbosity=2)