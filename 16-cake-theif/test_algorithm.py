import unittest
import main


class AlgorithmShould(unittest.TestCase):
    def test_should_buySix_threePoundCakes_andOne_twoPoundCakes(self):
        cake_tuples = [(7, 160), (3, 90), (2, 15)]
        capacity = 20

        max_value = main.max_duffel_bag_value(cake_tuples, capacity)

        self.assertEqual(max_value, 555)

    def test_should_buyTwo_threePoundCakes_andOne_fivePoundCake(self):
        cake_tuples = [(3, 40), (5, 70)]
        capacity = 9

        max_value = main.max_duffel_bag_value(cake_tuples, capacity)

        self.assertEqual(max_value, 120)

    def test_should_buyOneCake(self):
        cake_tuples = [(3, 40)]
        capacity = 3

        max_value = main.max_duffel_bag_value(cake_tuples, capacity)

        self.assertEqual(max_value, 40)


if __name__ == '__main__':
    unittest.main(verbosity=2)