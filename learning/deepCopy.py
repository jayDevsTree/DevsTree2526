import copy

# Deep copy changes happens only in new list original prevented

original_list = [[1,2,3],[4,5,6],[7,8,'a']]

print("Id of original_list: ", id(original_list))
print("Id of 1st element of original_list: ", id(original_list[0]))
print("Id of 2nd element of original_list: ", id(original_list[1]))
print("Id of 3rd element of original_list: ", id(original_list[2]))
print()

newlist = copy.deepcopy(original_list) # this is a deep copy
print("Id of newlist: ", id(newlist))
print("Id of 1st element of newlist: ", id(newlist[0]))
print("Id of 2nd element of newlist: ", id(newlist[1]))
print("Id of 3rd element of newlist: ", id(newlist[2]))
original_list[2][2]= 'jay'# this changes only in mentioned list changes in one not effect other
print("Original list: ",original_list)
print("New list: ",newlist)