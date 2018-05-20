import unittest
import main


class AlgorithmShould(unittest.TestCase):
    def test_find_valid_sums(self):
        flight_length = 5
        movie_lenghts = [3, 2]

        result = main.two_movies_sum_length(flight_length, movie_lenghts)
        self.assertTrue(result)

    def test_not_find_valid_sums(self):
        flight_length = 5
        movie_lenghts = [1, 2]

        result = main.two_movies_sum_length(flight_length, movie_lenghts)
        self.assertFalse(result)

    def test_not_use_first_number_twice(self):
        flight_length = 6
        movie_lenghts = [3, 1]

        result = main.two_movies_sum_length(flight_length, movie_lenghts)
        self.assertFalse(result)

    def test_not_use_last_number_twice(self):
        flight_length = 6
        movie_lenghts = [1, 3]

        result = main.two_movies_sum_length(flight_length, movie_lenghts)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main(verbosity=2)