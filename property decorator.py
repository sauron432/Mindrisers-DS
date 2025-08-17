class Student:
    def __init__(self, phy, chem, maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths
        # self.percentage = str(round((self.chem + self.maths + self.phy) / 3,2)) + "%" 
        
    # def calculatePercentage(self):
    #     self.percentage = str(round((self.chem + self.maths + self.phy) / 3,2)) + "%" 
    @property
    def percentage(self):    
        return str(round((self.chem + self.maths + self.phy) / 3,2)) + "%"
        
s1 = Student(88,90,78)
print(s1.percentage)  # Output: 85.33333333333333%

s1.phy = 78
# s1.calculatePercentage()
print(s1.percentage)  # Output: 92.0%