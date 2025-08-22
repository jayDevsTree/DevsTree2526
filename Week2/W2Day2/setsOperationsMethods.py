s1 = {1,2,3,2}
print(s1)

# All Set Commands and Operations in One Code

# Creating a Set
s = {1, 2, 3}
print("Create Set:", s)

s = set([1, 2, 3])
print("Create using set():", s)

# Adding Elements
s.add(4)
print("After add(4):", s)

# Removing Elements
s.remove(4)  # Raises error if not present
print("After remove(4):", s)

s.discard(5)  # No error if not present
print("After discard(5):", s)

print("Pop element:", s.pop())
print("After pop():", s)

# Clearing a Set
temp = s.copy()
temp.clear()
print("After clear():", temp)

# Copying a Set
copy_s = s.copy()
print("Copy of set:", copy_s)

# New sets for operations
a = {1, 2, 3}
b = {3, 4, 5}

# Union
print("Union:", a.union(b))

# Intersection
print("Intersection:", a.intersection(b))

# Difference
print("Difference (a-b):", a.difference(b))

# Symmetric Difference
print("Symmetric Difference:", a.symmetric_difference(b))

#  Subset & Superset
print("a is subset of b?:", a.issubset(b))
print("a is superset of b?:", a.issuperset(b))

#  Disjoint Sets
print("a and b are disjoint?:", a.isdisjoint(b))

#  Update Operations
c = {1, 2}
c.update({2, 3})
print("After update:", c)

c.intersection_update({2, 3})
print("After intersection_update:", c)

c.difference_update({3})
print("After difference_update:", c)

c.symmetric_difference_update({2, 4})
print("After symmetric_difference_update:", c)

#  Length and Membership
print("Length of set a:", len(a))
print("2 in a?:", 2 in a)
print("5 not in a?:", 5 not in a)
