
class BankAccount:

    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Invalid withdrawal amount!")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)

    def check_balance(self):
        print("Current Balance:", self.balance)

account1 = BankAccount(123456, 15000)

print("Account Number:", account1.account_number)

account1.deposit(10000)
account1.withdraw(5000)
account1.check_balance()
