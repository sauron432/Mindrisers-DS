class Car:
    def __init__(self, category):
        self.category = category
        
        
    @staticmethod
    def start():
        print("The car has started.")
        
    @staticmethod
    def stop():
        print("The car has stoppped.")
        
class Toyota(Car): # single inheritance
    brand = "Toyota"
    def __init__(self, model,category):
        # The line `super().__init__(category)` in the `Toyota` class is calling the `__init__` method
        # of the parent class `Car`. This line is used to initialize the `category` attribute of the
        # `Car` class when creating an instance of the `Toyota` class. By using `super()`, it ensures
        # that the `__init__` method of the parent class is called, allowing the `Toyota` class to
        # inherit and utilize the attributes and behavior defined in the `Car` class.
        super().__init__(category)
        self.model = model

car1 = Toyota("Rav4","SUV")
car2 = Toyota("Chaser","Sedan")

class LandCruiser(Toyota,Car): # Multiple inheritance
    def __init__(self, fuel, year):
        self.fuel = fuel
        self.year = year
        
car3 = LandCruiser("petrol",2021)

print("This is a ",car3.brand)
print(car3.brand)
print(car3.year)
car1.start()
car1.stop()


class A:
    varA = "welcome to class A"
class B:
    varB = "welcome to class B"
class C(A,B):
    varC = "Welcome to class C"
    
c1 = C()
print(c1.varA,c1.varB)
print(C.__mro__)


class Person:
    name = "UNKNOWN"
    
    def setName(self, a):
        self.name = a
        #Person.name = a # Modifies the class attribute
        #self.__class__.name = a # Modifies the class attribute
    @classmethod
    def changeName(cls, name):
        cls.name = name
    
p1 = Person()
p1.changeName("John")
print(p1.name)
print(Person.name)
