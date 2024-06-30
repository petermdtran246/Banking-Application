from Account import Account
from CoinCollector import CoinCollector
class Bank:
    max_bank_account = 100

    def __init__(self):
        self.accounts = [None] * self.max_bank_account

    # A method, ‘addAccountToBank’, that takes one parameter
    def addAccountToBank(self, account):
        """
        Adds an account to the bank, handling empty slots and capacity limitations.
        :parameter:
        --------------------------------
            account: An Account object to be added.
        :return:
        --------------------------------
            True if the account was added successfully, False otherwise.
        """
        for i in range(self.max_bank_account):
            if self.accounts[i] is None:
                self.accounts[i] = account
                return True
        print('No more accounts available')
        return False

    # A method, ‘removeAccountFromBank’, that takes one parameter
    def removeAccountFromBank(self, account):
        """
        Removes an account from the bank by matching account number.

        :parameter:
        --------------------------------------
            account: An Account object to be removed.
        :return:
        --------------------------------------
            True if the account was removed successfully, False otherwise.
        """
        for i in range(len(self.accounts)):
            current_account = self.accounts[i]
            if current_account is not None:
                account_matches = current_account.get_account_number() == account.get_account_number()
                if account_matches:
                    self.accounts[i] = None
                    return True
        return False


    # A method, ‘findAccount’ that takes one parameter
    def findAccount(self, account_number):
        """
        Finds an account by iterating through the bank's accounts and matching account numbers.

        :parameter:
        ------------------------------------
            accountNumber: The account number to search for.
        :return:
        ------------------------------------
            The Account object if found, None otherwise.
        """
        for account in self.accounts:
            if account is not None:
                account_matches = account.get_account_number() == account_number
                if account_matches:
                    return account
        return None
    
    # A method, ‘addMonthlyInterest’ that takes one parameter
    def addMonthlyInterest(self, annual_rate):
        """
        Adds monthly interest to all accounts based on the given annual interest rate.

        :parameter:
        ------------------------------------
            percent: The annual interest rate as a percentage.
        """
        monthly_rate = annual_rate / 12 / 100
        for account in self.accounts:
            balance = account.get_balance()
            interest = balance * monthly_rate
            account.deposit(int(round(interest)))
            print(
                f'Deposited interest: ${interest / 100:.2f} into account number: {account.get_account_number()}, '
                f'new balance: ${account.get_balance() / 100:.2f}')

