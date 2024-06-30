import random

class Account:
    def __init__(self, owner_first_name, owner_last_name, owner_ssn):
        """
        Initializes a new Account object with the provided owner details and generates a random account number and PIN.

        :parameter:
        ------------------------------------------------------------------
            owner_first_name: The owner's first name.
            owner_last_name: The owner's last name.
            owner_ssn: The owner's social security number (last 4 digits are displayed).
        """
        # Generate random 8 digits account number (not starting with 0)
        self.account_number = random.randint(10000000, 99999999 )
        self.owner_first_name = owner_first_name
        self.owner_last_name = owner_last_name
        self.owner_ssn = owner_ssn
        self.pin = '{:04d}'.format(random.randint(0, 9999)) # Random 4-digit PIN with leading zeros
        self.balance = 0
    
    # Add methods as getters and setters for attributes
    def get_account_number(self):
        return self.account_number

    def get_owner_first_name(self):
        return self.owner_first_name

    def set_owner_first_name(self, first_name):
        self.owner_first_name = first_name

    def get_owner_last_name(self):
        return self.owner_last_name

    def set_owner_last_name(self, last_name):
        self.owner_last_name = last_name

    def get_ssn(self):
        return self.owner_ssn

    def set_ssn(self, ssn):
        self.owner_ssn = ssn

    def get_pin(self):
        return self.pin

    def set_pin(self, pin):
        self.pin = pin

    def get_balance(self):
        return self.balance

    def set_balance(self, balance):
        self.balance = balance

    # A method ‘deposit’ that takes one parameter - an amount to deposit into the account as a ‘long’.
    def deposit(self, amount):
        """
        Deposits the given amount into the account and returns the updated balance.

        :parameter:
        -------------------------------------------------------
            amount: The amount to deposit (positive value).

        :returns:
        -------------------------------------------------------
            The updated account balance after the deposit.
        """
        self.balance += amount
        return self.balance

    # A method ‘withdraw’ that takes one parameter - an amount to withdraw from the account as a ‘long’
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True, self.balance
        else:
            return False, self.balance

    # A method ‘isValidPIN’ that takes one parameter – A String that represents a PIN
    def isValidPIN(self, pin):
        # Checks if the given PIN matches the account's PIN
        return self.pin == pin

    # all objects have a toString method - this indicates you are providing
    # your own version
    def __repr__(self):
        return (
            f'============================================================\n'
            f'Account Number: {self.account_number}\n'
            f'Owner First Name: {self.owner_first_name}\n'
            f'Owner Last Name: {self.owner_last_name}\n'
            f'Owner SSN: XXX-XX-{self.owner_ssn[-4:]}\n'
            f'PIN: {self.pin}\n'
            f'Balance: ${self.get_balance():.2f}\n'
            f'============================================================'
        )

