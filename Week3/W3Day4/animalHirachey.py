print("Animal Hirachey")

class Animal :
    def __init__(self):
        self.name = input("Enter Name of Animal: ")
    def sound(self):
        print("Sound")
    def get_name(self):
        return self.name
    
class Dog(Animal):
    def __init__(self):
        self.name = input("Enter Name of Dog: ")
    def sound(self):
        print("woof")
        
    def get_name(self):
        return self.name
    
class Cat(Animal):
    def __init__(self):
        self.name = input("Enter Name of Cat: ")
        
    def sound(self):
        print("Meow")
    
    def get_name(self):
        return self.name
    
class Bird(Animal):
    def __init__(self):
        self.name = input("Enter Name of Bird: ")
    
    def get_name(self):
        
        return self.name
    
D1 = Dog()
C1 = Cat()
B1 = Bird()

print(D1.get_name())
D1.sound()
print(C1.get_name())
print(B1.get_name())