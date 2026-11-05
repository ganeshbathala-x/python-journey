from abc import ABC, abstractmethod
class GardenEquipment(ABC):
    def __init__(self,name,status="ON"):
        self.name =name
        self.__status = status
    def get_status(self):
        return self.__status
    @abstractmethod
    def perform_action(self):
        pass

class WaterSpirinkler(GardenEquipment):
    def __init__(self,name,status,water_pressure):
        super().__init__(name,status)
        self.water_pressure = water_pressure
    def perform_action(self):
        print("The water sprinkler is watering the garden with pressure of",self.water_pressure)
        if self.get_status()== "ON":
            print("The water sprinkler is on.")
        else:
            print("THE water sprinkler is off")


class GardenLight(GardenEquipment):
    def __init__(self,name,status,light_brightness):
        super().__init__(name,status)
        self.light_brightness = light_brightness

    def perform_action(self):
        print("The garden light is illuminating the garden with brightness of ",self.light_brightness)
        if self.get_status()== "ON":
            print("The garden light is on.")
        else:
            print("THE garden light is off")
            
class Garden:
    def __init__(self):
        self.equipments =[]
    def add_equipment(self,equipment):
        self.equipments.append(equipment)
    def remove_equipment(self,equipment):
        self.equipments.remove(equipment)
    
class Gardener:
    def __init__(self,name): 
        self.name =name
        self.garden = Garden()
    def add_equipment(self,equipment):
        self.garden.add_equipment(equipment)
    def remove_equipment(self,equipment):
        self.garden.remove_equipment(equipment)

    def view_garden(self):
        for equipment in self.garden.equipments:
            print(equipment.name)
            equipment.perform_action()


ws=WaterSpirinkler("Sprinkler1",100,5)
gl=GardenLight("light1",50,10)

gardener=Gardener("John")
gardener.add_equipment(ws)
gardener.add_equipment(gl)
gardener.add_equipment(gl)
gardener.remove_equipment(gl)
gardener.view_garden()
# Day7
