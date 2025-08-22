
print("Implicit Type conversion that python does Automatically")
x = 10 
print("X Type:",type(x))
y = 18.0
print("Y Type:",type(y))
z = x+y
print("X+Y Type:",type(z))
print()

print("Explicit Type conversion that we have to do manually")
x = 10
print("X Type:",type(x))
y = float(x)
print("Y Type:",type(y))
z = int(x+y)
print("X+Y Type:",type(z))
print()

print("Type Conversion ASCII values")
a = chr(65)
print(a)

print()
print("Type Conversion string to binary to int) values")
# a = "1010"
# b = int(a,2)
# print(b)

def convert_to_int(s):
    try:
        convert_st = int(s,2)
        print(convert_st)
    except :
        print("Type Conversion not happen Invalid Input")
    finally:
        print("Function ends")
s = input("Enter binary value : ")
convert_to_int(s)
