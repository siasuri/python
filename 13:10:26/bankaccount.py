"""Aim:
To create a Python program using a BankAccount class and instance methods
to perform deposit, withdrawal, and balance-checking operations."""
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposit successful.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Withdrawal successful.")
        else:
            print("Insufficient balance.")

    def show_balance(self):
        print("Account holder:", self.name)
        print("Balance:", self.balance)


name = input("Enter account holder name: ")
balance = float(input("Enter opening balance: "))

account = BankAccount(name, balance)

deposit_amount = float(input("Enter amount to deposit: "))
account.deposit(deposit_amount)

withdraw_amount = float(input("Enter amount to withdraw: "))
account.withdraw(withdraw_amount)

account.show_balance()
