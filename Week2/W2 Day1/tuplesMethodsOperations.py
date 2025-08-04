print("Welcome to Coordinates System using tuples")


# tuple are Ordered , unmutable and Indexed 


tuple1 = (1,2,3,4)
print (tuple1)

t2 = (1,"Jay",2 , "Dhruv",3)
print(t2)
print(t2[1])
print(t2[:])

#using in keyword in tuple

t3 =(1,'jay', 2,'devarsh',3,'talha',4.0,'Dev',True)

for i in t3:
    print(i)

# for i in range (0,len(t3)):
#     print(t3[i])

if 'jay' in t3:
    print("Found")
else:
    print("Target Not Found")
    
    
# l1 =['JAY', "DEVARSH"]
# l1 = [item.lower() for item in l1 ]
# print(l1)

#tuple manipulation 

names = ("jay", "devarsh","talha")
tempNames = list(names)
tempNames[2] = "Dev"
tempNames.append("Dhruv")
names = tuple(tempNames)
print(names)

# tuple unpacking

tupleUnpack = ("Patil","Jay","SilverOak","university")
(surname, name , *collegeName ) = tupleUnpack
print("Name:", name)
print("College:",collegeName)