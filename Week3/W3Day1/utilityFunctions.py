def areaCalculation():
    
    userInput = (input('''1 --> Rectangle,
2 --> Triangle, 
3 --> Circle
: '''))
    
    try:
        userInput = int(userInput)
    except ValueError:
        print("Invalid Input")
        exit()
    
    match userInput:
        
        case 1:
            length_rec = float(input("enter Length of Rectangle: "))
            width_rec = float(input("Enter Width of Rectangle: "))
            area_rec = (length_rec * width_rec)
            
            if length_rec == width_rec:
                print(f"Square: {length_rec:0.2f} X {width_rec:0.2f} = {area_rec:0.2f} Units.")
            else:
                print(f"Rectangle: {length_rec:0.2f} X {width_rec:0.2f} = {area_rec:0.2f} Units.")
                
        case 2:
            
            height_tri = float (input("Enter Height of Triangle: "))
            base_tri = float(input("Enter Base of Triangle: "))
            area_tri = (height_tri * base_tri)/2
            print(f"Triangle: {height_tri:0.2f} X {base_tri:0.2f} = {area_tri:0.2f} Units.")
            
        case 3:
            
            radius_cir = float(input("Enter Radius of Circle: "))
            area_cir = (3.14 * radius_cir * radius_cir)
            print(f"Circle: {area_cir:0.2f} Units.")
        case _:
            print("Please Enter Valid Number")
            
# areaCalculation()

def tempConversion():
    
    userInput = (input('''1 --> Celsius to Fahrenheit,
2 --> Fahrenheit to Celsius
: '''))
    
    try:
        userInput = int(userInput)
    except ValueError:
        print("Invalid Input")
        exit()
    
    match userInput:
        
        case 1:
            celsius = float(input("Enter Celsius: "))
            fahrenheit = ((celsius * 9/5) + 32)
            print(f"{celsius:0.2f} Celsius = {fahrenheit:0.2f} Fahrenheit")
        case 2:
            fahrenheit = float(input("Enter Fahrenheit: "))
            celsius = ((fahrenheit - 32) * 5/9)
            print(f"{fahrenheit:0.2f} Fahrenheit = {celsius:0.2f} Celsius")
        case _:
            print("Please Enter Valid Number")
            
# tempConversion()

def dailyUtiliy():
    
    print("Utility Functions")
    print("1. Area Calculation")
    print("2. Temperature Conversion")
    
    userInput = input("Enter your choice: ")
    
    try:
        userInput = int(userInput)
    except ValueError:
        print("Invalid Input")
        exit()
    
    match userInput:
        
        case 1:
            areaCalculation()
        case 2:
            tempConversion()
        case _:
            print("Please Enter Valid Number")
            
dailyUtiliy()
            