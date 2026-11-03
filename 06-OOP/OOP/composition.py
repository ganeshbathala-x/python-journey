class Customer:
		def __init__(self,name):
			self.name =name
			
		def show_name(self):
			print(self.name)
			
class Order:
		def __init__(self,cname):
			self.cname=cname
			
		def show_customer(self):
			self.cname.show_name()
				
customer=Customer("Ravi")
order =Order(customer)
order.show_customer()