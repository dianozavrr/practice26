class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  

    def deposit(self, amount):
        self.__balance += amount   

    def withdraw(self, amount):
        self.__balance -= amount  

    def get_balance(self):
        return self.__balance    


account1 = BankAccount(100)

account1.deposit(351)
print("баланс після депозиту 351:", account1.get_balance())

account1.withdraw(100)
print("баланс після депозиту 100:", account1.get_balance())

account1.__balance = 0 
print("Баланс = 0:", account1.get_balance())
