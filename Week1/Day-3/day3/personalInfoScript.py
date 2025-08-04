# normal way
def info_taker():
    try:
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        height = float(input("Enter your height: "))
        married_input = input("Are you married (yes/no): ").strip().lower()#if user space or capital or small letter
        is_married = married_input == "yes"#only check yes == yes then Trueor otherwise False
    except:
        print("Invalid Input")
        return  
    print()
    print("Personal Information")
    print(name, ":", type(name))
    print(age, ":", type(age))
    print(height, ":", type(height))
    # True if married_input == "yes" else False
    # print(married_input, ":", type(married_input))
    print(is_married, ":", type(is_married))

info_taker()

# Efficient Way,
#  using dictionary

# personal_info ={
#     "name": input("Enter your name: "),
#     "age": int(input("Enter your age: ")),
#     "height": float(input("Enter your height: ")),
#     "married": input("Are you married (yes/no): ").strip().lower() == "yes"
# }

# print()
# print("Personal Information")
# print(personal_info["name"], ":", type(personal_info["name"]))
# print(personal_info["age"], ":", type(personal_info["age"]))
# print(personal_info["height"], ":", type(personal_info["height"]))
# print(personal_info["married"], ":", type(personal_info["married"]))
