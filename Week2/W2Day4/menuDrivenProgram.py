print("Welcome to Menu Driven Program,")
print("Here show some Patterns using for loops")

print('''1 --> Left Triangle
2 --> Right Triangle
3 --> Pyramid
4 --> Diamond
5 --> Hollow Diamond''')

input_choice = input("Enter your choice: ")

try:
    user_choice= int(input_choice)
except ValueError:
    print("Invalid Input")
    exit()
    
if user_choice in range (1,6):
    
    rows = int (input("Enter number of rows: "))
    print()

    match user_choice:
        case 1 :
            print("left Triangle")
            print()
            for i in range (0,rows):
                for j in range (0,i+1):
                    print("* ", end="")
                print()
                
            print()
        case 2 :
            
            print("Right Triangle")

            # for i in range(rows):
            #     print(" " * (rows - i - 1) + "*" * (i + 1))

            for i in range ( rows):
                print(" " * (rows - i - 1)*2 + " *" * (i + 1))
            print()
            
        case 3 :
            
            print("Pyramid")
            print()

            for i in range (rows):
                print(" " * (rows - i-1 ) + "*" * ((2*i)+1) + " " * (rows - i-1 ))
            print()
            
        case 4 :
            
            print("diamond")
            print()

            for i in range ( rows):
                print(" " * (rows - i - 1) + "*" * (2 * i + 1) + " " * (rows - i - 1))

            for i in range(rows-2 , -1 , -1): # range(start, stop, step) and row - 1 same level of uper triangle last line so -1 more(-1 + -1 = -2) is set in daimond and same like range lst element is exclude therefore -1 gone until 0 and , -1 represent range gone reverse order 
                print(" " * (rows - i - 1) + "*" * (2 * i + 1) + " " * (rows - i - 1))
        case 5 :
            
            print("Hollow Diamond")
            print()
            
            for i in range (rows):
                if i == 0:
                    print(" " * (rows - i-1 ) + "*")
                else:
                 print(" "*(rows-i-1)+ "*" + " "*(2*(i-1)+1) +"*" + " "*(rows-i-1) )
            for i in range(rows -2 ,-1,-1):
                if i == 0:
                    print(" "*(rows-1)+"*")
                else:
                    print(" "*(rows-i-1)+ "*" + " "*(2*(i)-1)+"*")
        case _ :
            print("Invalid Choice")
            
else:
    print("Invalid Choice")