print("This is a Example of custom exception,")

class DivideorMultiplyException(Exception):
    def __init__ (self,message):
        self.message = message
        
    def __str__(self):
        return f'{self.message}'
        
def divide_num(num1,num2):
    if num2 <=0 :
        raise DivideorMultiplyException("Divide by zero is not allowed")
    return num1/num2

def multi_num(num1,num2):
    if num1 == 0 or num2 == 0:
        raise DivideorMultiplyException("Multiply by zero is not allowed")
    return num1*num2

try:
    res = divide_num(10,0)
    print(res)
except DivideorMultiplyException as e:
    print('Message: ',e)
    
try:
    res = multi_num(10,10)
    print(res)
except DivideorMultiplyException as e:
    print('Message: ',e)
