
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
    
with open('Week4/W4Day1/sampleText.txt','w') as f3:
    f3.write("This line wrote from file write mode")
    f3.writelines("\nhello world")
    f3.writelines("\nThis line wrote from file writelines mode")
    
    
with open('Week4/W4Day1/sampleText.txt','a') as f4:
    f4.write("\nThis line wrote from file append mode")
    

with open('Week4/W4Day1/sampleText.txt', 'r') as f5:
    # print(f5.read())
    for line in f5:
        print(line.strip())
        

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

with open('Week4/W4Day1/sampleText.txt', 'r+') as f6:
    f6.write("\nThis line wrote from file write mode aaaaaaaaaa")
    f6.writelines("\nhello world\n")
    f6.seek(0)
    print(f6.read().strip())
    
with open ('Week4/W4Day1/sampleText.txt','w+') as f7:
    f7.write("This line writen from W+ mode\n")
    f7.writelines('this mode just do update fresh new Content \n')
    f7.seek(0)
    print(f7.read().strip())
    
with open('Week4/W4Day1/sampleText.txt','a+') as f8:
    f8.write("\nThis line writen from a+ mode")
    f8.seek(0)
    print(f8.read().strip())