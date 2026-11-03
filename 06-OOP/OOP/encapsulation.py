class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount


acc = Account("Ravi", 1000)
acc.deposit(500)
print(acc.owner, acc.get_balance())
