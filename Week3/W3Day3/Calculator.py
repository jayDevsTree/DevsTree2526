class Calculator:
    def __init__ (self):
        self.num = float(input("Enter Number: "))
        self.name = input("enter Name:")
        
    @staticmethod
    def greet(username):
        print(f"Hello {username}")
    
    def squareNum(self):
        print(f'Square : {(self.num*self.num):0.2f}')
        
    def cubeNum(self):
        print(f'Cube: {self.num*self.num*self.num:0.2f}')
    
    def squareRoot(self):
        print(f'Root: {(self.num**0.5):0.2f}')
    
c1 = Calculator()
c1.greet(c1.name)
# Calculator.greet(c1.name)
# c1.greet('jay')
c1.squareNum()
c1.squareRoot()
c1.cubeNum()