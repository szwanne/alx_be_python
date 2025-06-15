# Creating a class called BankAccount and initializing the account_balance
class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance
# Amount to be deposited into the bank

    def deposit(self, amount):
        self.account_balance >= amount
        return self.account_balance
# Comparing the amount to be withdraw to the amount

    def withdraw(self, amount):
        if (self.account_balance >= amount):
            self.account_balance -= amount
            return True
        else:
            return False
# The function will display the account balance

    def display_balance(self):
        return self.account_balance
