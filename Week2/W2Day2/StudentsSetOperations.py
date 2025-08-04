
GroupA = {'Jay', 'Devarsh', 'Dev', 'Dhruv'}

GroupB = {'veer', 'parth','Dhruv', 'talha'}

print('All Science Students GroupA + GroupB',GroupA.union(GroupB))

print('Some Students are in both groups:',GroupA.intersection(GroupB))


# res = GroupA-GroupB
# print("groupA-GroupB",res)

print("groupA - GroupB:",GroupA.difference(GroupB))

# res = GroupB-GroupA
# print("groupB-GroupA",res)
print("GroupB - GroupA:",GroupB.difference(GroupA))