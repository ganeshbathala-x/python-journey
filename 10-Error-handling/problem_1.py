class GameAccount:
    def __init__(self,username,coins):
        self.username=username
        self.coins=coins
    def purchase_item(self,price):
        if price <=0:
            raise ValueError("price must be graterthan zero")
        if price>self.coins:
            raise ValueError ("insufficient coins")
        self.coins-=price
        return self.coins

ga=GameAccount("leo",1000)

try:
    remaining=ga.purchase_item(300)
    print("purchase sucessfull")
    print("remaining conis:",remaining)
except ValueError as e:
    print("purchased failed",e)
else:
    print("purchased successfull")
finally:
    print("purchase purpose completed")