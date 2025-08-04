str = input("Enter string : ")
print("String:",str+"\n converting from string to diffent types,")
t = tuple(str)
print("tuple:", end=" ")
print(t)

l = list(str)
print("list:",l)

s = set(str)
print("set :",s)

# frequency of each character
d = dict()
for i in range (len(str)):
   char = str[i]
   d[char]= d.get(char,0)+1
print("dict:",d)