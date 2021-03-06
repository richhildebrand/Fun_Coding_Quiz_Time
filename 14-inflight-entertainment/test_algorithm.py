import unittest
import round2 as main


class AlgorithmShould(unittest.TestCase):
    def test_allow_to_of_the_same_number(self):
        flight_length = 5
        movie_lenghts = [7, 2, 7, 5, 3]

        result = main.two_movies_sum_length(flight_length, movie_lenghts)
        self.assertTrue(result)


    def test_find_valid_sums(self):
        flight_length = 5
        movie_lenghts = [3, 2]

        result = main.two_movies_sum_length(flight_length, movie_lenghts)
        self.assertTrue(result)

    def test_find_valid_sums_in_large_list(self):
        flight_length = 5
        movie_lenghts = [3, 7, 6, 11, 2, 13, 22]

        result = main.two_movies_sum_length(flight_length, movie_lenghts)
        self.assertTrue(result)

    def test_not_find_valid_sums(self):
        flight_length = 5
        movie_lenghts = [1, 2]

        result = main.two_movies_sum_length(flight_length, movie_lenghts)
        self.assertFalse(result)

    def test_not_find_valid_sums_in_large_list(self):
        flight_length = 5
        movie_lenghts = [1, 2, 6, 7, 11, 15, 19]

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