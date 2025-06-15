# Creating a class called BankAccount and initializing the account_balance
class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = round(float(account_balance), 2)
# Amount to be deposited into the bank

    def deposit(self, amount):
        self.account_balance += round(float(amount), 2)
        self.account_balance = round(float(amount), 2)
        return self.account_balance
# Comparing the amount to be withdraw to the amount

    def withdraw(self, amount):
        amount = round(float(amount), 3)
        if (self.account_balance >= amount):
            self.account_balance -= amount
            self.account_balance = round(self.account_balance, 2)
            return True
        else:
            return False
# The function will display the account balance

    def display_balance(self):
        return print(f"Current Balance: ${round((self.account_balance), 2)}")
