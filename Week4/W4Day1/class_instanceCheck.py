class Emp:
    
    empCount = 0
    
    def __init__ ( self,name,salary):
        self.name = name
        self.salary = salary
        Emp.empCount +=1
    
    def displayCount(self):
        print(f"Total employee :{Emp.empCount}")
    
    def empInfo(self):
        print("Name:{}, Salary:{}".format(self.name,self.salary))
        
e1 = Emp('jay', '90K')
e1.empInfo()
e1.age = 19
e1.displayCount()
e2 = Emp('Talha', '70k')
e2.empInfo()
e2.displayCount()
# print(Emp.empCount)
print(hasattr(e1,'empInfo')) # t
print(getattr(e1,'empCount')) #2 (cause at last total employee = 2)
print(setattr(e1,'age',22)) #None
print(getattr(e1,'age'))


class A :
    def myFun(self):
        print("In Class A")
        
class B(A):
    def myFun(self):
        print("In class B")
        
class C(A):
    def myFun(self):
        print("In Class C")
        
# class D(C,B): # ---> this print in Class C
#     pass
# sampleObj.myFun()

class D(B,C):# ---> this prints In class B
    pass

sampleObj = D()
sampleObj.myFun()   # the execition happens throught MRO(Method Resolution Order)
                    # class D(B, C) → checks D → B → C → A → object
                    # class D(C, B) → checks D → C → B → A → object
