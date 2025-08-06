import math
#wrong way cause default parameter must be at last
# def lecture_taler(name="Devarsh" , topic):
#     print("Hello {} today we learn {}".format(name,topic))
    
# lecture_taler('Data Science')
# lecture_taler("Jay","Python")

# right way
def lec_taler(name ,topic ='Data Science'):
    print("Hello {} today we learn {}".format(name,topic))
    
lec_taler('jay')
lec_taler("Jay","Python")
    
#keyword Arguments 
lec_taler(topic="Node",name="Devarsh")

#type of functions :
#1. Built-in functions
#2. User-defined functions

#type of arguments :
#1. Defalut arguments
#2. Keyword arguments
#3. Varieble-length  arguments
#    *args (variable-length non - keyword arguments)
#    **kwargs (variable-length keyword arguments)

# *args example --> recive tuple of arguments
def myFun(*nums):
    for i in nums:
        print(i , end =' ')
    print()
myFun(1,2,3,4,5,6)

# **kwargs example --> recive dictionary of arguments
def my_func(**topics):
    print("name = {} , topic = {}.".format(topics['name'],topics['topic']))
   
    
my_func(name='Jay', topic='Python')
my_func(name='Dhruv', topic='Data Science')

print(math.factorial(8))

def standard_arg(arg):
    print(arg)
standard_arg(10)        # OK
standard_arg(arg=10)    # OK

def pos_only_arg(arg, /):
    print(arg)
# pos_only_arg(10)        # OK
# pos_only_arg(arg=10)    # ERROR

def kwd_only_arg(*, arg):
    print(arg)
# kwd_only_arg(arg=10)    # OK
# kwd_only_arg(10)        # ERROR

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)
# combined_example(1, 2, kwd_only=3)         # OK
# combined_example(1, standard=2, kwd_only=3)# OK
# combined_example(pos_only=1, standard=2, kwd_only=3) # ERROR



