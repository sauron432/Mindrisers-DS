class A:
    def method(self):
        print("Method from A")

class B:
    def method(self):
        print("Method from B")

class C(A, B):
    def method(self):
        print("Method from C")
class E:
    def method(self):
        print("Method from E")

class D(C, B, E):
    def method(self):
        print("Method from D")

print(C.__mro__)
print(D.mro())

