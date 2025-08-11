class Bank:
    
    def __init__ (self,name,accountNo):
        self.name = name
        self.accountNo = accountNo
        self.balance = 0
        
    def deposit(self):
        amount = (input("Enter Amount to Deposit: "))
        try:
            valid_amount = float(amount)
            if valid_amount <= 0:
                raise BankExceptions.lessThanZeroDepositException()
        except BankExceptionChecker as valid:
            print("[Error]: ",valid)
            return
        except ValueError:
            print("Invalid Deposit Amount")
            return
        self.balance += valid_amount
        print(f"Deposit: {valid_amount:0.2f} deposited into Account Number {self.accountNo}.")
        return self.balance
    
    def withdraw(self):
        amount = (input("Enter Amount to Withdraw: "))
        try:
            valid_amount = float(amount)
            if valid_amount <= 0:
                raise BankExceptions.lessThanZeroWithdrawalException()
            
            if self.balance >= valid_amount:
                self.balance -= valid_amount
                print(f"Withdraw: {valid_amount:0.2f} withdrawn from Account Number {self.accountNo}.")
            else:
                raise BankExceptions.balanceGreaterThanWithdrawalException()
                print(f"Withdraw: {self.name} does not have enough balance!")
        except BankExceptionChecker as valid:
            print("[Error]: ",valid)
            return
        except ValueError:
            print("Invalid Withdrawal Amount")
            return
        return self.balance
    
    def show_balance(self):
        try:
            if self.balance < 0:
                raise BankExceptions.lessThanZeroBalanceException()
        except BankExceptionChecker as valid:
            print("[Error]: ",valid)
            return
        print(f"Total Balance: {self.name} has {self.balance:0.2f} in Account Number {self.accountNo}.")
        return self.balance

class BankExceptionChecker(Exception):
    def __init__ (self,message):
        self.message = message
    
    def __str__(self):
        return f'{self.message}'

class BankExceptions:
    
    @staticmethod
    def lessThanZeroDepositException():
        return BankExceptionChecker('Deposit amount should be greater than 0')
    
    @staticmethod
    def lessThanZeroWithdrawalException():
        return BankExceptionChecker('Withdrawal amount should be greater than 0')
    
    @staticmethod
    def lessThanZeroBalanceException():
        return BankExceptionChecker('Balance have never negative ')
    
    @staticmethod
    def validAmountException():
        return BankExceptionChecker('Amount should be greater than 0')
    
    @staticmethod
    def balanceGreaterThanWithdrawalException():
        return BankExceptionChecker('Balance should be greater than withdrawal amount')
    
obj = Bank('jay',2526)

print("Welcome to Bank Account Class,")
while True:
    print()
    print('''Methods:
1 --> Deposit
2 --> withdraw
3 --> balance
(press Anything Except(1/2/3)) --> Exit''')

    choice = input("Enter Choice: ")
    try:
        user_choice = int(choice)   
    except ValueError:
        print("Thank You!")
        exit()
    match user_choice:
        case 1:
            obj.deposit()
        case 2:
            obj.withdraw()
        case 3:
            obj.show_balance()
        case _:
            print("Exiting...")
            exit()