class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("баланс не може бути від’ємним")
        self.__balance = value

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("сума має бути додатною")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("сума має бути додатною")
        if self.balance - amount < 0:
            raise ValueError("недостатньо коштів")
        self.balance -= amount


acc = BankAccount(100)
print(acc.balance)
acc.deposit(50)
print(acc.balance)
