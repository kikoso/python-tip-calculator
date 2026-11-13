# Homework session 2 (challenge): account with deposit, withdraw and transfer


class InsufficientFundsError(Exception):
    pass


class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Betrag muss positiv sein")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Betrag muss positiv sein")
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Es fehlen {amount - self.balance} EUR")
        self.balance -= amount

    def transfer(self, other, amount):
        self.withdraw(amount)
        other.deposit(amount)


if __name__ == "__main__":
    a = Account(100)
    b = Account()
    a.transfer(b, 30)
    print(a.balance, b.balance)
    try:
        a.transfer(b, 500)
    except InsufficientFundsError as e:
        print(e)
