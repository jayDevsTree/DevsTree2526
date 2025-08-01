s1 = []
s1.append(1)#add multiply values
s1.insert(1,2) #first index second value
s1.insert(2,2)
s1.pop()
s1.remove(2)
s1.append(9)


s2=[1,2,3,4,5]
s1.extend(s2)

s1.sort()

s1.sort(reverse=True)
# s1.reverse()
print(s1.count(1))

print(s1.index(2))

# s1.clear()
# del s1;
print(s1)
for i in range(0,len(s1)):
    print(s1[i],end=" ")
print()   
s2 = [1,2,3,4,5]
s2 [0:3] = [0,0,0]
print(s2)



names = ['Jay', 'Patil', 'Dhruv', 'Prajapati', 'vrutik', 'koladiya', 'rajesh', 'suthar', ]
# names_v=[]
# for i in names:
#     if 'v' in i and len(i)>5:
#             names_v.append(i)

# print(names_v)

names_j = [name for name in names if 'j' in name.lower()]
print(names_j)


