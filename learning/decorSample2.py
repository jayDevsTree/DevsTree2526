# suppose a function that addition of two numbers  and i required 3 number sum in that case that function may not be imported or not accesble in my code due to protected or other reason in that case i need to  use a decorator and need that function and modify it as per my need


def decor(add):
    def inner():
        print("This is a Decorator function,")
        res = add() # this is a existing code
        num3 = float(input("Enter third Number:"))
        res +=num3
        
        return res
    return inner
        
        

@decor # --> add = decor(add)
def add():
    print("This is a add function")
    
    num1 = float (input("Enter First Number:"))
    num2 = float (input("Enter second Number:"))
    result = num1 + num2
    
    return result

print(add())
