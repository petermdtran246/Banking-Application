import random

class BankUtility:
    
    def __init(self):
        pass

    # A method ‘promptUserForPositiveNumber’ that takes one parameter
    def promptUserForString(self, prompt):
        """
        Prompts the user for a string input and returns it.

        :parameter:
        -----------------------------------
            prompt: A string representing the message to display to the user.

        :return:
        -----------------------------------
            The user's input as a string.
        """
        user_input = input(prompt)
        return user_input.strip()

    # A method ‘convertFromDollarsToCents’ that takes one parameter
    def promptUserForPositiveNumber(self, prompt):
        """"
        Prompts the user for a positive number and validates the input.

        :parameter:
        -------------------------------------
            prompt: A string representing the message to display to the user.

        :returns:
        -------------------------------------
            A positive number entered by the user as a float.
        """
        while True:
            try:
                number = float(input(prompt))
                if number > 0:
                    return number
                else:
                    print('Amount cannot be negative. Try again.')
            except ValueError:
                print('Invalid input. Please enter a number.')

    # A method ‘generateRandomInteger’ that takes two parameters
    def generateRandomInteger(self, min, max):
        """
        Generates a random integer within a specified range (inclusive).

        :parameter:
        ---------------------------------------------------
            min: The minimum value for the random integer.
            max: The maximum value for the random integer.

        :return:
        ----------------------------------------------------
            A random integer between min_value and max_value (inclusive).
        """
        return random.randint(min, max)

    @staticmethod
    def convertFromDollarsToCents(amount):
        """
        Converts a dollar amount to its equivalent in cents (long integer).

        :parameter:
        --------------------------------------
            amount: The amount in dollars as a float.

        :return:
        --------------------------------------
            The amount in cents as a long integer.
        """
        return int(round(amount * 100))


    def isNumeric(self, numberToCheck):
        try:
            float(numberToCheck)
            return True
        except ValueError:
            return False
