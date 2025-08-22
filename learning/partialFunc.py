from functools import partial

def add(a,b,c,d):
    return a+b+c+d

add = partial(add,a=1,b=2)
print(add(c=3,d=4))

print("-------")
#when we need that some values are fix during the function call we use partial real life example is interest rate is fix for all users
def rate_of_interest(p,r,t):
    return p*r*t/100

roi = partial(rate_of_interest,r=3.6)
print(roi(p=10000,t=2))
print(roi(p=20000,t=3))