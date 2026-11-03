from abc import ABC,abstractmethod

class FitnessActivity(ABC):
	def __init__(self,name,duration,calories):
		self.name=name
		self.duration=duration
		self.__calories=calories
	def get_calories(self):
		return self.__calories
	@abstractmethod
	def calculate_calories(self):
		pass
		
class Running(FitnessActivity):
	def __init__(self,name,duration,calories):
		super().__init__(name,duration,calories)
	def calculate_calories(self):
		total_calories=self.get_calories()-(self.duration*100)
		return total_calories
		
class Cycling(FitnessActivity):
	def __init__(self,name,duration,calories,weight):
		super().__init__(name,duration,calories)
		self.weight=weight

	def calculate_calories(self):
		total_calories=self.get_calories()-(self.weight%self.duration)
		return total_calories

class Swimming(FitnessActivity):
	def __init__(self,name,duration,calories,gender):
		super().__init__(name,duration,calories)
		self.gender=gender
			
	def calculate_calories(self):
		if self.gender =="Male":
			total_calories=self.get_calories()-(self.duration*20)+10
		else:
			total_calories=self.get_calories()-(self.duration*10)+5
			
		return total_calories
		
class FitnessTracker:
	def __init__(self):
		self.activities=[]
	def add_activity(self,activity):
		self.activities.append(activity)
	def remove_activity(self,activity):
		self.activities.remove(activity)
	def total_all_calories(self):
			total=0
			for activity in self.activities:
				total+=activity.calculate_calories()
			return total
				
class User:
	def __init__(self,name):
				self.name=name
				self.fitness_tracker=FitnessTracker()
	def view(self):
		for act in self.fitness_tracker.activities:
			print(act.name,act.calculate_calories())
		
		print(self.fitness_tracker.total_all_calories())
		
run=Running("ravi",60,2000)
run.calculate_calories()
cycle=Cycling("Rahul",120,5000,75)
cycle.calculate_calories()
swim=Swimming("ramu",100,7000,"Male")
swim.calculate_calories()
ft=FitnessTracker()
ft.add_activity(run)
ft.add_activity(cycle)
ft.add_activity(swim)
ft.remove_activity(cycle)
ft.total_all_calories()
user=User("gani")
user.fitness_tracker=ft
user.view()

				


		