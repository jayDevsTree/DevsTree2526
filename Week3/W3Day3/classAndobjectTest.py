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


    
