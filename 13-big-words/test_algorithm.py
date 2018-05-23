import unittest
import round2 as main


class AlgorithmShould(unittest.TestCase):
    ###count steps
    def test_find_rotation_point_in_middle(self):
        word_list = ['ccc', 'aaa', 'bbb']
        rotation_point_index, steps_to_find_point = main.find_rotation_point(word_list)
        self.assertEqual(rotation_point_index, 1)
        self.assertEqual(steps_to_find_point, 1)

    def test_find_rotation_point_at_start(self):
        word_list = ['aaa', 'bbb', 'ccc']
        rotation_point_index, steps_to_find_point = main.find_rotation_point(word_list)
        self.assertEqual(rotation_point_index, 0)
        self.assertEqual(steps_to_find_point, 1)

    def test_find_rotation_point_at_end(self):
        word_list = ['bbb', 'ccc', 'aaa']
        rotation_point_index, steps_to_find_point = main.find_rotation_point(word_list)
        self.assertEqual(rotation_point_index, 2)
        self.assertEqual(steps_to_find_point, 1)

    def test_find_rotation_point_second_from_last(self):
        word_list = ['f', 'g', 'h', 'i', 'j', 'a', 'b']
        rotation_point_index, steps_to_find_point = main.find_rotation_point(word_list)
        self.assertEqual(rotation_point_index, 5)
        self.assertEqual(steps_to_find_point, 3)

    def test_find_rotation_point_second_from_start(self):
        word_list = ['g', 'a', 'b', 'c', 'd', 'e', 'f']
        rotation_point_index, steps_to_find_point = main.find_rotation_point(word_list)
        self.assertEqual(rotation_point_index, 1)
        self.assertEqual(steps_to_find_point, 2)

    ###compare words
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