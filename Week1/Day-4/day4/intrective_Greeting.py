def greeting_person():
    number_of_person = int ( input("Enter number of person : "))
    for i in range (number_of_person):
        name = input(f"Enter {i+1}th person name: ")
        age = int(input(f"Enter {i+1}th person age: "))
        
        if age <= 18 and age >= 0:
            print(f"hey! {name} you are {age} years old\n")
        elif(age >= 18):   
            print(f"respected {name} you are {age} years old\n")
        else:
            print("invalid age")
greeting_person()


def simple_greeting():
    simple_uname= input("Enter your name: ")
    simple_age = int(input("Enter your age: "))
    print(f"{simple_uname} : {simple_age} years old")
# simple_greeting()