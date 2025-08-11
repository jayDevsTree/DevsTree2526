import csv

with open('Week4/W4Day1/sampleFileCSV.csv', 'r') as f:
    
    ro = csv.reader(f,delimiter=',')
    data = list(ro)
    print(data)    
    
    print()
    print("Printing Data Row by Row,")
    for row in data:
        print(row)
        
    print("printing data in column by column")
    for col in zip(*data):
        print(col)
        
    # print()
    # print("print data of colum 1")
    # for col in data:
    #     print(col[0])
    
def append_csv(): 
    l1 = [['1@2@3'], ['4@5@6'], ['7@8@9']]
    with open('Week4/W4Day1/sampleFileCSV.csv', 'a+') as f:
        wo = csv.writer(f,delimiter='@')  
        wo.writerows(l1)
        
        f.seek(0)
        print(f.read())
    l2 = [['10$11$12'], ['13$14$15'], ['16$17$18']]
    with open('Week4/W4Day1/sampleFileCSV.csv', 'a+') as f:
        wo = csv.writer(f,delimiter='$')
        wo.writerows(l2)
        
        f.seek(0)
        print(f.read())
append_csv()