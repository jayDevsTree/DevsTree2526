
class Employee:
    def __init__(self):
        self.name = input("Enter Name:")
    def calculate_salary(self):
        pass
    
class Manager(Employee):
    def __init__(self):
        super().__init__()# this is a super keyword
        self.monthly_salary = float(input("Enter Salaray:"))
    
    def calculate_salary(self):
        return self.monthly_salary
    
class Intern(Employee):
    def __init__(self):
        super().__init__()
        self.monthly_stipend = int(input("Enter Stipend:"))
        
    def calculate_salary(self):
        return self.monthly_stipend
    
class Developer(Employee):
    def __init__(self):
        super().__init__()
        self.hourly_charge = int(input("Enter Hourly Charge:"))
        self.daily_hours = int(input("Enter Hours for Work:"))
        
    def calculate_salary(self):
        return (self.hourly_charge*self.daily_hours)
        
employees =[
    # Employee(),
    Manager(),
    Intern(),
    Developer()
]

for emp in employees:
    print(f'{emp.name} salary : {emp.calculate_salary()}')