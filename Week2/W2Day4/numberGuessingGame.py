print("Welcome to number Guessing Game,")
print('''You just Enter Number And hint shared Accrording to your Input,
      if you enter negative number it will convert into positive number!''')

target = abs(int(input("Enter Target Number: ")))# abs convert negative number to positive



def NumberGuesser():
    guess = None
    while (guess!=target):
        
        try:
            guess = abs(int(input("Enter Number: "))) # for checking we stay first String
        except ValueError:
            print("Invalid Input")
            return
        # user_Guess =(input("Enter Number: "))   # for checking we stay first String
        # if not user_Guess.isdigit(): # but not effiecient for negative numbers
        #     print("Invalid Input")
        #     return
        # guess = abs(int(user_Guess))# after checking right input we convert into integer
        
        if guess == target:
            print(f'''You Found It
{target} is your Target Number!''')
            break
        elif abs(guess -target) <= 5 :
            if guess < target:
                print("close Guess little Higher")
            else:
                print("close Guess little Lower")
        elif guess < target:
            print ("Higher")
        else:
            print("Low")
            
NumberGuesser()
            