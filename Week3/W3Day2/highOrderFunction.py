def square(x):
    return x * x

def cube(x):
    return x * x * x

def apply_function(func, number):
    return func(number)
num = int(input("Enter a number: "))
print('Square:',apply_function(square, num))  
print('Cube:',apply_function(cube, num))   


def square(x):
    return x * x

numbers = [1, 2, 3, 4]
result = list(map(square, numbers))# map and also use of lambda
print(result)


def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
result = list(filter(is_even, numbers))# filter with function use
print(result)




def operate_on_list(func, data):
    result = []
    for item in data:
        result.append(func(item))
    return result

def double(x):
    return x * 2
print(operate_on_list(double, [1, 2, 3]))



def apply_function(func, a, b):
    return func(a, b)

print(apply_function(lambda x, y: x + y, 5, 3))
print(apply_function(lambda x, y: x * y, 5, 3))
