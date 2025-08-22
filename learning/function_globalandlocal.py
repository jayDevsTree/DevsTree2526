a = 10

def greet(name):
    b = 5
    print(f"Hello {name}")
    
greet("Jay")


globals()['a'] = 100# this change the value of global variable

print(globals())
print("------------------")

locals()['b'] = 200 # this change the value of local variable
print(locals())
print("------------------")
print()
print("dir:")
print(dir())
