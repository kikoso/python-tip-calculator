# Exceptions 3: account with your own exception


class InsufficientFundsError(Exception):
    pass


class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Betrag muss positiv sein")
        if amount > self.balance:
            missing = amount - self.balance
            raise InsufficientFundsError(f"Es fehlen {missing} EUR")
        self.balance -= amount


acc = Account(100)
acc.withdraw(30)
print(acc.balance)

try:
    acc.withdraw(500)
except InsufficientFundsError as e:
    print(e)
