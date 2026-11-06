class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def __str__(self):
        return f"Product: {self.name}, Price: ₹{self.price}, Quantity: {self.quantity}"


p1=Product("laptop",50000,1)
print(p1)