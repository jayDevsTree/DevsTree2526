
def Outer():
    x = 100
    
    def inner():
        x = 200
        return x
    return inner

inner = Outer()
print(inner())

print("--------")
def outer_fun():
    print("hello")
    
    def inner_fun():
        print("bye")
        
    return inner_fun

inner_fun = outer_fun()
inner_fun()