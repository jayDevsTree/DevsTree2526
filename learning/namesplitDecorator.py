
def name_upper_decor(func):
    def inner():
        return func().upper()
    return inner

def split_name(func):
    def inner():
        return func().split()
    return inner

@split_name
@name_upper_decor
def name_input():
    name = input("Enter First Name:")
    lname = input("Enter Last name:")
    full_name = name + " " + lname
    return full_name
    
print(name_input())