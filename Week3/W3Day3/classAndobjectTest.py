class ItComapany:
    company = 'DevsTree'
    
jay = ItComapany()
iterns_status = jay.company
print(iterns_status)

class DevsTree:
    
    role = "Python Developer"
    
    def __init__(self , name):
        self.name = name
        
    def Training(self):
        print(f'{self.name} learning {self.role}')
        
o1 = DevsTree('jay')
o1.Training()


    
class Programmer:
    def __init__ (self,name,id,role,company):
        self.name = name
        self.id = id
        self.role = role
        self.company = company
    def info(self):
        print(f'{self.name} in {self.company} and role {self.role} have id {self.id}')
        
        
e1 = Programmer('jay',57,'python','DevsTree')
e1.info()

class Programmer2:
    def __init__ (self):
        self.name = input("Enter Name: ")
        self.id = input("Enter Id: ")
        self.role = input("Enter Role: ")
        self.company = input("Enter Company: ")
    def info(self):
        print(f'{self.name} in {self.company} and role {self.role} have id {self.id}')
        
        
e1 = Programmer2()
e1.info()


       
        