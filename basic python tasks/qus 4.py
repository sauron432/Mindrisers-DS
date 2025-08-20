from abc import abstractmethod,ABC

class Shape(ABC):
    def area():
        pass
    def perimeter():
        pass
    
class Rectangle(Shape):
    def __init__(self,length,breath):
        self.length = length
        self.breath = breath
        
    def area(self):
        return self.length * self.breath
        
    def perimeter(self):
        return 2 * (self.length + self.breath)
    
# MAIN PROGRAM STARTS
rect1 = Rectangle(10,20)
print("Area:",rect1.area())
print('Perimeter:',rect1.perimeter())

rect2 = Rectangle(25,15)
print("Area:",rect2.area())
print('Perimeter:',rect2.perimeter())