from abc import ABC,abstractmethod
class Vehicle(ABC):
		@abstractmethod
		def start(self):
			pass
			
class Car(Vehicle):
		def start(self):
			print("Car starts with key")
		
class Bike (Vehicle):
		def start(self):
			print("Bike starts with button")
			
car =Car()
bike =Bike()

car.start()
bike.start()
