class CoinCollector:
    def __init__(self):
        pass

    @staticmethod
    def parseChange(coins):
        """
        Calculate the amount it represents in cents as a 'long' and return it.

        :parameter:
        -------------------
            coins = A string representing the coins (P, N D, Q, H, W)

        :return:
        --------------------
            The total value of the coins in cents
        """

        total_value = 0
        coin_value = {
            'P': 1, # Penny
            'N': 5, # Nickel
            'D': 10, # Cents
            'Q': 25, # Quarters
            'H': 50, # Half-dollar
            'W': 100, # Whole dollar
        }

        for coin in coins: # Convert coin string to uppercase for case-insensitive matching
            if coin in coin_value:
                total_value += coin_value[coin]
        return total_value


