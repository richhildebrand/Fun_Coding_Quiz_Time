import unittest
import main


class AlgorithmShould(unittest.TestCase):
    def test_find_None_when_no_items_are_in_stack(self):
        stack = main.MaxStack()
        max_value = stack.get_max()
        self.assertEqual(max_value, None)

if __name__ == '__main__':
    unittest.main(verbosity=2)