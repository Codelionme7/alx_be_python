## bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize the BankAccount object.
        initial_balance (float): Starting balance, defaults to 0.
        """
        # This is an attribute (variable) unique to each instance of the class
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        self.account_balance += amount

    def withdraw(self, amount):
        """
        Deduct the amount if funds are sufficient.
        Returns True if successful, False if insufficient funds.
        """
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Print the current balance in a user-friendly format."""
        # The :.2f ensures it prints with 2 decimal places (like money)
        print(f"Current Balance: ${self.account_balance:.2f}")