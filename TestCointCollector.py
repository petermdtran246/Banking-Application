from CoinCollector import CoinCollector
import unittest

class TestCoinCollector(unittest.TestCase):
    # 1st Unit Test
    def test_parseChange_empty_string(self):
        total_value = CoinCollector.parseChange('')
        self.assertEqual(total_value, 0)

    # 2nd Unit Test
    def test_parseChange_multiple_coins(self):
        total_value = CoinCollector.parseChange('PNDQH')
        self.assertEqual(total_value, 91)

    # 3rd Unit Test
    def test_parseChange_single_coin(self):
        total_value = CoinCollector.parseChange('N')
        self.assertEqual(total_value, 5)

if __name__ == '__main__':
    unittest.main()