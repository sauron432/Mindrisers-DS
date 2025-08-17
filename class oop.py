class Student:
    uni = "Kathmandu University" #Class attribute. Stays the same for all the objects that are created from this class.
    country = "India"

    def __init__(self, roll:int, name:str, age:int, reg_num: int):
        '''
        Initialise the new object. Pass roll, name, age, and reg_num as arguments.
        '''
        #Instance attributes. New for every object that is created.
        self.roll = roll
        self.name = name
        self.age = age
        self.registration_number = reg_num

    def __str__(self):
        return f"Roll: {self.roll}\nName: {self.name}\nAge: {self.age}\nRegistration Number: {self.registration_number}\ncountry: {self.country}\nUniversity: {self.uni}\n"
    
    def introduce(self):
        '''
        Prints the basic introduction of the student.
        '''
        print("This is the introduction of the student:")
        print(f"My name is {self.name} from {self.country}. I am a student of {self.uni} with registration number {self.registration_number}.")
        
    def set_country(self,new_country)-> None:
        self.country = new_country
    
    def get_country(self):
        return self.country
        
        
student1 = Student(130,"John Doe",21,45434)
student1.introduce()
print(student1)
student1.set_country("Dhulikhel")
print(student1)

student2 = Student()

    