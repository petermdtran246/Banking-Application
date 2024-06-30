from Account import Account
import unittest

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account('Peter', 'Tran', '999999999')

    # Unit Test for Deposit
    def test_deposit(self):
        self.assertEqual(self.account.deposit(2000), 2000)
        self.assertEqual(self.account.deposit(3000), 5000)

    # Unit Test for isValidPin
    def test_is_valid_pin(self):
        pin = self.account.get_pin()
        self.assertTrue(self.account.isValidPIN(pin))
        self.assertFalse(self.account.isValidPIN('67896'))

if __name__ == '__main__':
    unittest.main()