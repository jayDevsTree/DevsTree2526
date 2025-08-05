def ageCatergorySpecifier(age):
    if age < 0:
        print("Invalid age")
    elif age >= 0 and age <= 5:
        print("Baby")
    elif age <= 5:
        print("Toddler")
    elif age <= 12:
        print("Child")
    elif age <= 17:
        print("Teen")
    elif age >=60:
        print("Senior")
    else:
        print("Adult ")

age = int(input("Enter your age: "))
ageCatergorySpecifier(age)