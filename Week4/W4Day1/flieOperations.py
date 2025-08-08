f1= open('Week4/W4Day1/sampleText.txt', 'r')
read_line = f1.readline()

f1.seek(0) # this go file starting because it update pointer everytime
read_lines = f1.readlines()

f1.seek(0)
read_everything = f1.read()
print('readline(): ',read_line)
print('readlines(): ',read_lines) # stores as a List of each lines
print('read(): ',read_everything)

f1.seek(0)
print()
print("Using Loop,")
for line in f1:
    print(line.strip())

f1.close()

print()
print("Best Way to read file using With open as,")

with open('Week4/W4Day1/sampleText.txt', 'r') as f2:
    print('readlines: ',f2.readlines())
    f2.seek(0)
    print()
    print("using Loops,")
    for line in f2:
        print(line.strip())
        
    f2.seek(0)
    print('read() ',f2.read())
    
    f2.seek(0)
    print('readline() ',f2.readline)
    
    
       
        
    