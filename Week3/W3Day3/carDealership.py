import csv

# Load company list from CSV
with open('carCompaines.csv', 'r') as f:
    reader = csv.DictReader(f)
    comapany_list = [row['company'].lower() for row in reader]

# Custom Exception
class validNameAndComapany(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return f'{self.message}'

# Exception Checker Class
class validNameAndComapnyChecker:
    @staticmethod
    def invalidName():
        return validNameAndComapany("Invalid model! Enter Valid Model.")

    @staticmethod
    def invalidCompany():
        return validNameAndComapany("Invalid Company! Enter Valid Company.")

# Car Class
class Car:
    
    def __init__(self, name, company, model, year):
        self.name = name
        self.company = company
        self.model = model
        self.year = year

    def display_info(self):
        print(f'Company: {self.company}')
        print(f'Model: {self.model}')
        print(f'Year: {self.year}')

# Dealership Class
class Dealership:
    def __init__(self):
        self.inventory = {}

    def input_car_details(self):
        IsvalidName = False
        IsvalidComp = False

        # Company validation
        while not IsvalidComp:
            try:
                company = input("Enter Company: ")
                if company.lower() not in comapany_list:
                    raise validNameAndComapnyChecker.invalidCompany()
                IsvalidComp = True
            except validNameAndComapany as valid:
                print("[Error]:", valid)
                print("Enter a valid company")

        # Model validation
        while not IsvalidName:
            try:
                model = input("Enter model: ")
                if model.lower() in comapany_list:
                    raise validNameAndComapnyChecker.invalidName()
                IsvalidName = True
            except validNameAndComapany as valid:
                print("[Error]:", valid)
                print("Enter a valid model")

        # Year validation
        while True:
            try:
                year = int(input("Enter Year: "))
                if 1800 <= year <= 2025:
                    break
                else:
                    print("Enter year between 1800 and 2025")
            except ValueError:
                print("Invalid Year! Enter Valid Year.")

        return Car(company, model, year)

    def add_car(self):
        car_input = self.input_car_details()
        if car_input.model not in self.inventory:
            self.inventory[car_input.model] = car_input
            print(f'Successfully Added {car_input.model} in Inventory')
        else:
            print("Car already exists!")

    def display_all_cars(self):
        if not self.inventory:
            print("Inventory is Empty")
        else:
            print("Current Inventory:")
            for item in self.inventory.values():
                item.display_info()

    def remove_car(self):
        car_remove_input = input("Enter Car model to remove: ")
        if car_remove_input in self.inventory:
            del self.inventory[car_remove_input]
            print(f'Car {car_remove_input} removed from Inventory.')
        else:
            print("Car not found")

    def search_car(self):
        search_car = input("Enter model of Car to search: ")
        car = self.inventory.get(search_car)
        if car:
            print("Car Found")
            car.display_info()
        else:
            print("Car Model Not Found")

    def update_car(self):
        update_car_model = input("Enter Car model to update: ")
        if update_car_model in self.inventory:
            print("Enter (Updating) Details:")
            updated_car = self.input_car_details()
            self.inventory[update_car_model] = updated_car
            print(f'{update_car_model} car details updated!')
        else:
            print("Car Not Found!")

# Main Controller
def Controlcode():
    deal = Dealership()
    while True:
        print('\n----- Car Dealership Inventory System -----')
        print('''
        1 --> Add Car
        2 --> Display All Cars
        3 --> Remove Car
        4 --> Search Car
        5 --> Update Car
        (press anything else to Exit)''')

        user_choice = input("Enter Choice: ")

        try:
            user_choice = int(user_choice)
        except ValueError:
            print("Thank You!")
            break

        if user_choice == 1:
            deal.add_car()
        elif user_choice == 2:
            deal.display_all_cars()
        elif user_choice == 3:
            deal.remove_car()
        elif user_choice == 4:
            deal.search_car()
        elif user_choice == 5:
            deal.update_car()
        else:
            print("Thank You!")
            break



if __name__ == '__main__':
    Controlcode()
