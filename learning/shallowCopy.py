import copy 

# shallow copy changes happens in both original and new list

mylist = [[1, 2, 3], [4,5,6], [7,8,'a']]
print("Id of mylist: ", id(mylist))
print("Id of 1st element of mylist: ", id(mylist[0]))
print("Id of 2nd element of mylist: ", id(mylist[1]))
print("Id of 3rd element of mylist: ", id(mylist[2]))
print()
# newlist = mylist  # this is also create shallow copy
newlist = copy.copy(mylist) # this is a shallow copy
print("Id of newlist: ", id(newlist))
print("Id of 1st element of newlist: ", id(newlist[0]))
print("Id of 2nd element of newlist: ", id(newlist[1]))
print("Id of 3rd element of newlist: ", id(newlist[2]))
# mylist[2][2]= 'jay'# this chanbes in both original and new list
print("Original list: ",mylist)
print("New list: ",newlist)
