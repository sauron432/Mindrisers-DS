class Person:
    scientific_name = "Homo sapiens" # class attribute 
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}\nFROM PERSON CLASS"
    
    def __repr__(self):
        pass
    
    def change_age(self , new_age:int):
        self.age = new_age
        
    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
        
class ABC:
    pass

class Doctor(ABC, Person): #Inheritance

    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def introduce(self):
        super().introduce()        
        # MRO 
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}\nFROM DOCTOR CLASS"

p1 = Person("John",30)
p2 = Person("Jane",31)
d1 = Doctor("Dr. Ram", 65)

d1.introduce()

# for p in [p1,p2,p3,p4,p5]:
#     print(p)

p1.introduce()
print(f"Before update:{p1.age}")
p1.change_age(22)
print("After update:",p1.age,sep="|")
print(p2)
print(Person.scientific_name)
print(d1)

print(Doctor.mro())