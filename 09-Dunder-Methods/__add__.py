class BankAccount:
    def __init__(self,onwer,balance):
        self.onwer=onwer
        self.balance=balance
    def __add__(self,other):
        return self.balance+other.balance
acc1=BankAccount("ganesh",500)
acc2=BankAccount("ramu",200)
print(acc1+acc2)