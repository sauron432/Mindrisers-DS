class Car:
    no_of_wheels = 4 #class attribute as a car always has 4 wheels. Shared by all the objects of Car class. Can be overridden
    # brand = "MUSTANG"
    def set_info(self,model:str, brand:str,color:int,power:int,seats:int, fuel_type: str)-> None:
        '''
        Set the information of the object. Pass model name, brand name, color, power, number of seats and the fuel type of the car for every instance created.
        '''
        #Instance or object attributes. Unique for each new instances that are created.
        self.brand = brand
        self.color = color
        self.power = power
        self.no_of_seats = seats
        self.fuel_type = fuel_type
        self.model = model
    
    def get_info(self)-> None:
        '''
        Get the info of the object. Returns the attributes of the instance.
        '''
        print(f"Model:{self.model}\nBrand:{self.brand}\nColor:{self.color}\nPower:{self.power}\nFuel Type:{self.fuel_type}\nNumber of seats:{self.no_of_seats}\nNumber of wheels:{self.no_of_wheels}")
        
    def __str__(self):
        return "This is the '__str__' function. It returns a string representation of the object."

car1 = Car()
car1.set_info("A45 S","Mercedes","Silver",480,5,"Petrol")
car1.get_info()
print(car1)# calls the __str__ methond. Works like car1.__str__().

car2 = Car()
car2.set_info("Ioniq 5","Hyundai","Grey",140,5,"Electric")
car2.get_info()

print(car2.brand)
del car2.brand
# print(car2.brand)

print(dir(int))