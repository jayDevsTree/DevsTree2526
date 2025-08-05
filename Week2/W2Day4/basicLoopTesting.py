users = {
    'jay': 'Active',
    'Devarsh': 'Inactive',
    'Dev': 'Active',
    'talha': 'Inactive',
    'Dhruv': 'Active',
    'veer': 'Inactive'
}


for  user , status in users.copy().items():
    if status == 'Inactive':
        print(user)
        
print(list (filter(lambda i : users[i]=='Inactive',users)))

inactive_users_list1 = [user for user in users.copy() if users[user] == 'Inactive']
inactive_users_list2 = [ user for user, status in users.items() if status == 'Inactive']
print(inactive_users_list1)
print(inactive_users_list2)

l1 = list(range(0,11))
print(l1)
evenNumbers_l1 = [ i for i in l1 if i %2 == 0]
print(evenNumbers_l1)

# # this finds all possible factors of given range
def factorOfGivenRange():
    print("Range->",range(2,10))
    for i in range (2,10):
        for j in range (2,i):
            if i % j == 0:
                print(f"{i} = {j} * {i //j}")
factorOfGivenRange()
            
#prime number find in range 

def showerFactorOrPrime():
    print()
    print(f"Range-> {range(2,10)} finds prime number")
    for n in range(2,10):
        for x in range ( 2, n):
            if n % x == 0 :
                print(f"{n} = {x} * {n//x}")
                break # because fpr prime check we need only find one factor if there then it definitely not prime
                
        else:
            print(f"{n} is a prime number")      
showerFactorOrPrime()

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
print(http_error(418))