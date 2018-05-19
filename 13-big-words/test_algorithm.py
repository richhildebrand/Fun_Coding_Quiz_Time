import unittest
import main


class AlgorithmShould(unittest.TestCase):
    def test_a_should_come_before_b(self):
        firstWordIsFirst = main.first_word_is_first_alphabetically('a', 'b')
        self.assertTrue(firstWordIsFirst)


if __name__ == '__main__':
    unittest.main(verbosity=2)