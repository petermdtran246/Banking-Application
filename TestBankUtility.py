from BankUtility import BankUtility
import unittest

class TestBankUtility(unittest.TestCase):
    def setUp(self):
        self.bank_utility = BankUtility()

    # Unit Test for isNumeric
    def test_isNumeric(self):
        self.assertFalse(self.bank_utility.isNumeric('abcd'))
        self.assertFalse(self.bank_utility.isNumeric('45646werew456'))
        self.assertTrue(self.bank_utility.isNumeric('123456789'))
        self.assertTrue(self.bank_utility.isNumeric('0'))

    # Unite Test for generateRandomInteger
    def test_generateRandomInteger(self):
        result = self.bank_utility.generateRandomInteger(10, 20)
        self.assertIn(result, range(10, 21))

if __name__ == '__main__':
    unittest.main()



