class Wallet:
    def __init__(self,onwer,balance):
        self.onwer=onwer
        self.balance=balance
    def add_money(self,amount):
        self.balance+=amount
    def __bool__(self):
        return self.balance>0

wallet=Wallet("ganesh",500)
wallet.add_money(200)
empty=Wallet("ramu",0)
print(bool(wallet))
print(bool(empty))
