import unittest
import main


class AlgorithmShould(unittest.TestCase):
    def test_a_should_come_before_b(self):
        firstWordIsFirst = main.first_word_is_first_alphabetically('a', 'b')
        self.assertTrue(firstWordIsFirst)

    def test_b_should_not_come_before_a(self):
        firstWordIsFirst = main.first_word_is_first_alphabetically('b', 'a')
        self.assertFalse(firstWordIsFirst)

    def test_aa_should_come_before_ab(self):
        firstWordIsFirst = main.first_word_is_first_alphabetically('aa', 'ab')
        self.assertTrue(firstWordIsFirst)

    def test_ab_should_not_come_before_aa(self):
        firstWordIsFirst = main.first_word_is_first_alphabetically('ab', 'aa')
        self.assertFalse(firstWordIsFirst)

    def test_aa_should_come_before_aaa(self):
        firstWordIsFirst = main.first_word_is_first_alphabetically('aa', 'aaa')
        self.assertTrue(firstWordIsFirst)

    def test_aaa_should_not_come_before_aa(self):
        firstWordIsFirst = main.first_word_is_first_alphabetically('aaa', 'aa')
        self.assertFalse(firstWordIsFirst)



if __name__ == '__main__':
    unittest.main(verbosity=2)