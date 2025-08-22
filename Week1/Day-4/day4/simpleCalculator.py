def simpleCalculator():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    
    operator = input("Enter operator(+,-,*,/,%): ")
    
    if operator == '+':
        print(a+b)
    elif operator == '-':
        print(a-b)
    elif operator == '*':
        print(a*b)
    elif operator == '/':
        if b!=0:
            print(a/b)
        else:
            print("Cannot divide by zero")
    elif operator == '%':
        if(b!=0):
            print(a%b)
        else:
            print("Cannot module by zero")
    else:
        print("Invalid Operator")   
        
simpleCalculator()