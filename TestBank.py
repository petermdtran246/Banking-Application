from Account import Account
from Bank import Bank
import unittest

class TestBank(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()
        self.account1 = Account('Peter', 'Tran', '999999999')

    # Unit Test for addAccountToBank
    def test_findAccount(self):
        # Create an Account object
        self.bank.addAccountToBank(self.account1)
        self.assertEqual(self.bank.findAccount(self.account1.account_number), self.account1)
        self.assertIsNone(self.bank.findAccount(12345678))

    def test_addMonthlyInterest(self):
        self.bank.addAccountToBank(self.account1)
        self.account1.deposit(20000)  # $200.00
        self.bank.addMonthlyInterest(6)  # 6% annual interest rate
        self.assertAlmostEqual(self.account1.get_balance(), 20100)

if __name__ == '__main__':
    unittest.main()