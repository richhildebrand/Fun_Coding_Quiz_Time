import unittest
import main as main

class OurTests(unittest.TestCase):
 
    def test_arrayWithMin_BeforeMax(self):
        stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
        result = main.get_max_profit(stock_prices_yesterday)
        assert result == 6

    def test_arrayWithMin_AfterMax(self):
        stock_prices_yesterday = [10, 12, 5, 8, 11, 9]
        result = main.get_max_profit(stock_prices_yesterday)
        assert result == 6

    def test_WithoutUsing_MaxValue(self):
        stock_prices_yesterday = [11, 22, 15, 8, 20, 3]
        result = main.get_max_profit(stock_prices_yesterday)
        assert result == 12

    def test_WithoutUsing_MinValue(self):
        stock_prices_yesterday = [10, 30, 5, 8, 20, 3]
        result = main.get_max_profit(stock_prices_yesterday)
        assert result == 20

if __name__ == '__main__':
    unittest.main()