import unittest
import main


class AlgorithmShould(unittest.TestCase):
    def test_find_None_when_no_items_are_in_stack(self):
        stack = main.MaxStack()
        max_value = stack.get_max()
        self.assertEqual(max_value, None)

    def test_find_max_when_we_do_not_pop(self):
        stack = main.MaxStack()
        stack.push(3)
        stack.push(7)
        stack.push(5)

        max_value = stack.get_max()

        self.assertEqual(max_value, 7)

if __name__ == '__main__':
    unittest.main(verbosity=2)