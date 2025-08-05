t1 = (1,2,3)
print(t1)
# t1[0]= 10 # tuple is immutable
temp = list(t1)
temp[0]= 10
t1 = tuple(temp)
print(t1)

l1 =(list(range(0,11)))
print(l1)
l1.append(1)
print(l1)
tempSet = set(l1)
l1 = list(tempSet)
print(l1)   

s = set() 
s.add(20) 
s.add(20.0) 
s.add('20') 
print(len(s))# 2 

s={}
print(type(s))

friend_dict = {}

# for i in range(4):
#     print("Enter name of friend",i+1)
#     name = input()
#     print("enter Language of Friend",i+1)
#     language = input()
#     friend_dict[name]= language

# print(friend_dict)

# s = {8, 7, 12, "Harry", [1,2]}

# tempchanger = list(s)
# s[4]=[2,3]
# s = set(tempchanger)
# print(s)# can not set indexed therefore error happen

# num_list = []
# for i in range (4):
#     num = int(input("Enter number: "))
#     num_list.append(num)
# num_list.sort()

# print(num_list[-1])

#Write a program to find out whether a student has passed or failed if it requires a 
#total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
#take marks as an input from the user.

# marks= []
# isPass = True
# for i in range(3):
#     marks_student = int(input("enter marks:"))
#     if marks_student < 33:
#         isPass = False
#         print("Fail")
#         break
#     else:
#         marks.append(marks_student)
# if isPass:
#     print("Percentage:",sum(marks)/3)
#     if (sum(marks)/3) < 40:
#         print("Fail")
#     else:
#         print("Pass")
        
#A spam comment is defined as a text containing following keywords: 
#“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
#to detect these spams.

spam_words= ['make a lot of money', 'buy now', 'subscribe this', 'click this']

msg = input("Enter a Message:")
isspam = False
for spam in spam_words:
    if spam in msg:
        isspam = True
        break
    else:
        continue
if isspam==True :
    print("Spam Detected!")
else:
    print("Not a Spam")
