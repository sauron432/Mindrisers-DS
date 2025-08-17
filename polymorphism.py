class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, num2):
        return Complex(self.real + num2.real, self.imaginary + num2.imaginary)
    
    def __sub__(self, num):
        return Complex(self.real - num.real, self.imaginary - num.imaginary)
    
    def show(self):
        print(f"{self.real}+{self.imaginary}j")

print(10+25)
print("Hello " + "World!")
        
num1 = Complex(1,6)
num2 = Complex(2,7)

num1.show()
num2.show()
# complexa = complex(a)
# complexb = complex(b)
# num3 = complexa + complexb
# print(num3)

# a = 2 + 3j
# b = 2 + 3j
# print(a+b)