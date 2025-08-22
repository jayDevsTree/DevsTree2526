print("Here show some Patterns using for loops")
rows = int (input("Enter number of rows: "))

print("Pattern 1: left Triangle")
print()
for i in range (0,rows):
    for j in range (0,i+1):
        print("* ", end="")
    print()
    
print()
print("Pattern 2: Right Triangle")

# for i in range(rows):
#     print(" " * (rows - i - 1) + "*" * (i + 1))

for i in range ( rows):
    print(" " * (rows - i - 1)*2 + " *" * (i + 1))
    
# for i in range(rows):
#     for j in range(rows - i - 1):
#         print(" ", end="") # end ='' use to stay on same line use
#     for k in range(i + 1):
#         print("*", end="")
#     print()

print()
print("Pyramid:")
print()

for i in range (rows):
    print(" " * (rows - i-1 ) + "*" * ((2*i)+1) + " " * (rows - i-1 ))



print()
print("diamond:")
print()

for i in range ( rows):
    print(" " * (rows - i - 1) + "*" * (2 * i + 1) + " " * (rows - i - 1))

for i in range(rows-2 , -1 , -1): # range(start, stop, step) and row - 1 same level of uper triangle last line so -1 more(-1 + -1 = -2) is set in daimond and same like range lst element is exclude therefore -1 gone until 0 and , -1 represent range gone reverse order 
    print(" " * (rows - i - 1) + "*" * (2 * i + 1) + " " * (rows - i - 1))
    
print("Hollow Diamond:")
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