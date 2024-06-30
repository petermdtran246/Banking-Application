from Account import Account
from Bank import Bank
from BankUtility import BankUtility
from CoinCollector import CoinCollector

class BankManager:
    def __init__(self):
        self.bank = Bank()

    @staticmethod    
    def promptForAccountNumberAndPIN(bank):
        while True:
            account_number = input('Enter account number: ')
            account = bank.findAccount(int(account_number))

            if account is None:
                print(f'Account not found for account number: {account_number}')
            else:
                pin = input('Enter PIN: ')
                if account.isValidPIN(pin):
                    return account
                else:
                    print('Invalid PIN')

    def main(self):
        while True:
            # Display menu options
            print('===========================================================')
            print('Welcome to Bank Management System')
            print('1. Open a new account')
            print('2. Get account information and balance')
            print('3. Change PIN')
            print('4. Deposit money into account')
            print('5. Transfer money between accounts')
            print('6. Withdraw money from an account')
            print('7. Make an ATM withdrawal from an account')
            print('8. Deposit change into an account')
            print('9. Close an account')
            print('10. Add monthly interest to all accounts')
            print('11. Exit')
            print('============================================================')
            # Get user choice
            choice = input('Enter your choice (1-11): ')
            # Validate and handle user choice
            if choice.isdigit():
                choice_int = int(choice)
                if 1 <= choice_int <= 11:
                    # Call appropriate method based on choice
                    if choice_int == 1:
                        self.open_new_account()
                    elif choice_int == 2:
                        self.get_account_info()
                    elif choice_int == 3:
                        self.change_pin()
                    elif choice_int == 4:
                        self.deposit_funds()
                    elif choice_int == 5:
                        self.transfer_funds()
                    elif choice_int == 6:
                        self.withdraw_funds()
                    elif choice_int == 7:
                        self.atm_withdrawal()
                    elif choice_int == 8:
                        self.deposit_change()
                    elif choice_int == 9:
                        self.close_account()
                    elif choice_int == 10:
                        self.add_monthly_interest()
                    elif choice_int == 11:
                        print('End Program')
                        break
                else:
                    print('Invalid choice. Please enter a number between 1 and 11.')
            else:
                print('Invalid choice. Please enter a number.')

    def open_new_account(self):
        # Prompts user for account details
        first_name = input("Enter Account Owner's First Name: \n")
        last_name = input("Enter Account Owner's Last Name: \n")
        ssn = input("Enter Account Owner's SSN (9 digits): \n")

        if len(ssn) != 9 or not ssn.isdigit():
            print('Social Security Number must be 9 digits')
            return

        new_account = Account(first_name, last_name, ssn)
        if self.bank.addAccountToBank(new_account):
            print('Account successfully created.')
            print(new_account)
        else:
            print('Failed to create a new account. Bank may be at maximum capacity.')

    def get_account_info(self):
        account = self.promptForAccountNumberAndPIN(self.bank)
        if account is not None:
            print(account)

    def change_pin(self):
        account = self.promptForAccountNumberAndPIN(self.bank)
        if account:
            while True:
                new_pin = input('Enter your new PIN: ')
                if not new_pin.isdigit():
                    print(f'{new_pin} is not a number.')
                elif len(new_pin) != 4:
                    print('PIN must be 4 digits, try again.')
                else:
                    confirm_pin = input('Reenter new PIN again to confirm: ')
                    if new_pin == confirm_pin:
                        # Update account PIN and inform user
                        account.set_pin(new_pin)
                        print('PIN updated successfully')
                        break
                    else:
                        print('PINs do not match, try again.')

    def deposit_funds(self):
        account = self.promptForAccountNumberAndPIN(self.bank)
        if account:
            amount = float(input('Enter amount to deposit in dollars and cents (e.g. 2.57): '))
            if amount <= 0:
                print('Deposit amount must be positive. Try again.')
                return
            cents = BankUtility.convertFromDollarsToCents(amount)
            account.deposit(cents)
            print(f'New balance: ${amount:.2f}')

    def transfer_funds(self):
        from_account = self.promptForAccountNumberAndPIN(self.bank)
        if from_account:
            to_account_number = input('Account to Transfer To: ')
            to_account = self.bank.findAccount(int(to_account_number))
            if to_account:
                amount = float(input('Enter amount to transfer in dollars and cents (e.g. 2.57): '))
                if amount <= 0:
                    print('Transfer amount must be positive. Try again.')
                    return
                cents = BankUtility.convertFromDollarsToCents(amount)
                if from_account.withdraw(cents):
                    to_account.deposit(cents)
                    print('Transfer complete')
                    print(f'New balance in account {from_account.account_number} is: ${amount:.2f}')
                    print(f'New balance in account {to_account.account_number} is: ${amount:.2f}')
                else:
                    print('Insufficient funds in your account')
            else:
                print('Destination account not found')

    def withdraw_funds(self):
        account = self.promptForAccountNumberAndPIN(self.bank)
        if account:
            amount = float(input('Enter amount to Deposit in dollars and cents (e.g. 2.57): '))
            if amount <= 0:
                print('Withdrawal amount must be positive.')
                return
            if account.withdraw(BankUtility.convertFromDollarsToCents(amount)):
                print(f'New balance ${amount:.2f}.')
            else:
                print('Insufficient funds')

    def atm_withdrawal(self):
        account = self.promptForAccountNumberAndPIN(self.bank)
        if account:
            amount = int(input('Enter amount to withdraw in dollars (no cents) in multiples of $5 (limit $1000)'))
            if amount < 5 or amount > 1000 or amount % 5 != 0:
                print('Invalid amount. Try again.')
                return
            twenties = amount // 20
            amount %= 20
            tens = amount // 10
            amount %= 10
            fives = amount // 5
            amount %= 5

            cents = BankUtility.convertFromDollarsToCents(amount)
            if account.withdraw(cents):
                print(f'Number of 20-dollar bills: {twenties}')
                print(f'Number of 10-dollar bills: {tens}')
                print(f'Number of 5-dollar bills: {fives}')
                print(f'New balance: ${account.get_balance() / 100:.2f}')
            else:
                print('Insufficient funds')

    def deposit_change(self):
        account = self.promptForAccountNumberAndPIN(self.bank)
        if account:
            change = input('Deposit coins: ')
            try:
                cents = CoinCollector.parseChange(change)
                account.deposit(cents)
                print(f'${cents / 100:.2f} in coins deposited into account.')
                print(f'New balance: ${account.get_balance() / 100:.2f}')
            except ValueError:
                print('Invalid coin.')

    def close_account(self):
        account = self.promptForAccountNumberAndPIN(self.bank)
        if account:
            self.bank.removeAccountFromBank(account)
            print(f'Account {account.get_account_number()} closed')

    def add_monthly_interest(self):
        annual_rate = float(input('Enter annual interest rate percentage (e.g. 2.75 for 2.75%): '))
        self.bank.addMonthlyInterest(annual_rate)
        print('Monthly interest added to all accounts successfully')

if __name__ == '__main__':
    manager = BankManager()
    manager.main()
















