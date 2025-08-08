x = lambda a : a +10
print(x(5))

multiple = lambda a,b : a*b
print(multiple(6,7))

maxOfTwo = lambda a,b : a if a>b else b
print(maxOfTwo(10,20))

l1 = [2,3,1,7,9,5]

secondLargest_l1 = lambda num : sorted(l1)[-2] 
print(secondLargest_l1(l1))

l2 = [[3,4,1,0],[8,99,32],[2,4,5] ]

sort_sublist = lambda original_list : [sorted(sublist) for sublist in original_list]
secondLargest_l2 = lambda originalList :[ secondLargest_sublist[-2] for secondLargest_sublist in sort_sublist(originalList)]  
print(secondLargest_l2(l2))

tables = [i for i in range(1,11)]

print(tables)

table_print = lambda number:[number*iterable for iterable in range(1,11)]
print(table_print(5))

numbers = [ 1,2,3,4,5]
squared = list(map(lambda x : x*x , numbers))
print("Map: ",squared)

names = ['jay','j ', 'jj', 'hh','de','   d   ', 'Dhruv', 'meet']

names_strip = list(map(lambda name : name.strip(), names))
moreThanThree = list(filter(lambda name : len(name)>=3,names_strip))
print("Filter: ",moreThanThree)

print('Sorted(length) :',list(sorted(names, key = lambda x : len(x))))
print('Sorted(length with strip) :',list(sorted(names_strip, key = lambda x : len(x))))
