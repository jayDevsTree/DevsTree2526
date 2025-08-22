import math



print("Coordinates Distant find in 2 Tuples")



#formula of Ditance between two coordinates are D = √[(x2 – x1)^2 + (y2 – y1)^2]

def twoCoordinateDistanceFinder():

    x1 = float(input("Enter X1 value:"))
    y1 = float(input("Enter Y1 value:"))
    tuple1 = (x1,y1)
    x2 = float(input("Enter X2 value:"))
    y2 = float(input("Enter Y2 value:"))
    tuple2 = (x2,y2)


    distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
    # distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

    print(f"Distance of ({x1:0.1f} , {y1:0.1f}) To ({x2:0.1f} , {y2:0.1f}): {distance:0.2f} Units.")
    
    
twoCoordinateDistanceFinder()

