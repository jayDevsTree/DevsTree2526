print("Welcome to Bank Account Class,")

class BankAccount:
    
    def __init__(self, name, bankAccountNo):
        self.name = name
        self.bankAccountNo = bankAccountNo
        self.Totalbalance = 0.0  # initialize balance to 0

    def deposit(self):
        amount = float(input("Enter Amount to Deposit: "))
        self.Totalbalance += amount
        print(f"Deposit: {amount:0.2f} deposited into Account Number {self.bankAccountNo}.")
    
    def withdraw(self):
        amount = float(input("Enter Amount to Withdraw: "))
        if self.balance() >= amount:
            self.Totalbalance -= amount
            print(f"Withdraw: {amount:0.2f} withdrawn from Account Number {self.bankAccountNo}.")
        else:
            print(f"Withdraw: {self.name} does not have enough balance!")

    def balance(self):
        print(f"Total Balance: {self.name} has {self.Totalbalance} in Account Number {self.bankAccountNo}.")
        return self.Totalbalance

# Example Usage
user1 = BankAccount('Jay', 2526)
while True:
    print('''Methods:
    1 --> Deposit
    2 --> withdraw
    3 --> balance
    (press Anything Except(1/2/3)) --> Exit''')
    choice = (input("Enter Choice:"))
    try :
        user_choice = int(choice)
    except ValueError:
        print("Thank You!")
        exit()

    if user_choice == 1:
        user1.deposit()
    elif user_choice == 2:
        user1.withdraw()
    elif user_choice == 3:
        user1.balance()

