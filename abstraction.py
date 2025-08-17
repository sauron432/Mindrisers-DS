from abc import abstractmethod,ABC

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "BARK!!!"

class Cat(Animal):
    def sound(self):
        return "MEOW!!!"
    
dog = Dog()
print(dog.sound())

cat = Cat()
print(cat.sound())