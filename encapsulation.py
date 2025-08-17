# class Student:
#     @staticmethod
#     def college():
#         print("Gaand Faad College")

class Car:
    def __init__(self):
        self.accelerator = False
        self.brake = False
        self.clutch = False
        
    def start(self):
        self.clutch = True
        self.accelerator = True
        print("Car is ready to go vroom vroom")
        
# car1 = Car()
# car1.start()

#Private attributes
class Account:
    def __init__(self, acc_num: float, acc_pin):
        self.account_number = acc_num
        self.__account_pin = acc_pin # This is a private attributre as it starts with '__'
    
    def reset_pin(self):
        print(self.__account_pin)
        
acc_1 = Account(405150,2010)
print(acc_1.account_number)
acc_1.reset_pin()
# print(acc_1.__account_pin)


class Person:
    __name = "Anonymous"
    
    def __hello(self):
        print("Hello from the other side.")
    
    def welcome(self):
        self.__hello() #Private scopes are only accessible within the class they are defined in.
        
p1 = Person()
p1.welcome()
# print(p1.__name) # This will throw an error as __name is a private attribute and
p1.welcome()
# p1.__hello()
