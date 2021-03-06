import unittest
import round2 as main


class AlgorithmShould(unittest.TestCase):
    def test_find_None_for_max_when_no_items_are_in_stack(self):
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

    def test_allow_us_to_pop(self):
        stack = main.MaxStack()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        stack.pop()
        result = stack.pop()

        self.assertEqual(result, 2)

    def test_allow_us_to_pop_and_still_know_max(self):
        stack = main.MaxStack()
        stack.push(1)
        stack.push(2)
        stack.push(6)
        stack.push(5)

        max_value = stack.get_max()
        self.assertEqual(max_value, 6)

        stack.pop()
        max_value = stack.get_max()
        self.assertEqual(max_value, 6)

        stack.pop()
        max_value = stack.get_max()
        self.assertEqual(max_value, 2)

    def test_allow_us_to_use_the_same_max_multiple_times(self):
        stack = main.MaxStack()
        stack.push(1)
        stack.push(5)
        stack.push(6)
        stack.push(6)

        max_value = stack.get_max()
        self.assertEqual(max_value, 6)

        stack.pop()
        max_value = stack.get_max()
        self.assertEqual(max_value, 6)

        stack.pop()
        max_value = stack.get_max()
        self.assertEqual(max_value, 5)


if __name__ == '__main__':
    unittest.main(verbosity=2)