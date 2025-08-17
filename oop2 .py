class Vehilce:
    cls = "VEHICLE"    
    Cylinders = 4
    wheels = 4
    driver_seat = 1
    fuel_type = "Petrol"
    
    def start(self):
        print("The vehicle has started.")
        
    def move(self):
        print("The vehicle is moving.")
    
    def stop(self):
        print("The vehicle has stopped.")
        
    def __str__(self):
        
        return f"This is a {self.Cylinders} object."
        
class Truck(Vehilce):
    wheels = 12
    fuel_type = "Diesel"
    cls = "TRUCK"
    
class Car(Vehilce):
    wheels = 4
    type = "Car"
    cls = "CAR"
    def gettype(self):
        return self.type    
    
    
class Toyota(Car,Vehilce):
    country_of_origin = "Japan"
    cls = "Toyota"
    def __init__(self, model, year):
        self.model = model
        self.year = year
    
    def country(self):
        return self.country_of_origin
        
truck_1 = Truck()
truck_1.start()
print(truck_1)

c1 = Car()
print(c1.gettype())
c1.start()

toyota1 = Toyota("Camry",2019)
print(toyota1.country())
toyota1.start()
print(toyota1.cls)
# print(Vehilce)

print(Toyota.mro())