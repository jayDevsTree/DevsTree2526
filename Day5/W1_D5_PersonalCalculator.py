def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def calculator():
    print("Welcome to Personal Calculator")
    print()
    print('''
        1 --> Add
        2 --> Subtract
        3 --> Multiply
        4 --> Divide
        (press anything else to Exit)''')
    
    user_choice = input("Enter Choice: ")
    try:
        user_choice = int(user_choice)
    except ValueError:
        print("Thank You!")
        exit()
    
    if user_choice not in [1, 2, 3, 4]:
        print("Thank You!")
        exit()

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if user_choice == 1:
        print("Result:", add(num1, num2))
    elif user_choice == 2:
        print("Result:", subtract(num1, num2))
    elif user_choice == 3:
        print("Result:", multiply(num1, num2))
    elif user_choice == 4:
        print("Result:", divide(num1, num2))
    else:
        print("Invalid choice!")

if __name__ == '__main__':
    calculator()
