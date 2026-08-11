# Q1 :  Create a BankAccount class with attributes account_number, owner_name, and balance.
# Add methods to deposit, withdraw, and check balance.


class BankAccount:
    def __init__(self, account_number, owner_name, balance):  # instance atribute
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"deposited: {amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"withdraw: {amount}")
        else:
            print("Insufficient balance")

    def check_balance(self):
        print(f"your current balance: {self.balance}")


u1 = BankAccount(1223, "Ramim", 10_000)
u1.deposit(2000)
u1.withdraw(3000)
u1.check_balance()
