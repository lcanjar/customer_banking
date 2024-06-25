""" Create a Account class with methods"""

class Account:
    """Creating an Account class with methods"""
    def __init__(self, balance, interest, months):
        self.balance = balance
        self.interest = interest
        self.months = months

    # This method sets the balance of the account.
    def set_balance(self, balance):
        """Sets the balance for the for the account"""
        self.balance = balance

    # The method sets the interest gained for the account.
    def set_interest(self, interest):
        """Sets the interest gained for the the account"""
        self.interest = interest

    # The method gets the balance gained for the account.
    def get_balance(self):
        """Gets the interest gained for the the account"""
        return self.balance 

# The method gets the interest gained for the account.
    def get_interest(self):
        """Gets the interest gained for the the account"""
        return self.interest