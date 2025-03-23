

class Vehicle(): # Base class 
    def __init__(self ,brand ,model , year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_specs(self):
        print("Brand", self.brand)
        print("Model",self.model)
        print("year",self.year)
        


class Car(Vehicle):
    def __init__(self,brand ,model,year,door):
        super().__init__(brand ,model ,year)
        self.door = door 
        self.distance = 0


    def milage(self,distance):
        self.distance += distance
        print("Distance Travelled---",self.distance)

    
    def get_specs(self):
        super().get_specs()
        print("Doors",self.door)



class Bus(Vehicle):
    def __init__(self,brand ,model,year,seater):
        super().__init__(brand ,model ,year)
        self.seater = seater 
        self.distance = 0


    def milage(self,distance):
        self.distance += distance
        print("Distance Travelled---",self.distance)

    
    def get_specs(self):
        super().get_specs()
        print("Mo of seats ",self.seater)





car1 = Car("Tata","nexon","2023","4",)
car1.get_specs()

print("--------------------\n")

bus1 = Bus("Volvo","v1","2020","50")
bus1.get_specs()
