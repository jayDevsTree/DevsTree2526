def add_student(grades):
    name = input("Enter student name: ")
    try:
        marks = float(input("Enter student grade: "))
    except ValueError:
        print("Invalid grade. Try again.")
        return
    grades[name] = marks
    print(f"{name}'s grade added.")

def view_students(grades):
    if not grades:
        print("No student data available.")
        return
    print("\nStudent Marks")
    for name, grade in grades.items():
        print(f"{name}: {grade}")
        
def delete_student(grades):
    name = input("Enter student name to delete: ")
    if name in grades:
        del grades[name]
        print(f"{name}'s data deleted.")
    else:
        print(f"{name} not found in student data.")

def calculate_average(grades):
    if not grades:
        print("No grades to calculate average.")
        return
    avg = sum(grades.values()) / len(grades)
    print(f"Average Marks: {avg:.2f}")

def grade_manager():
    grades = {}
    while True:
        print('''
--- Student Grade Manager ---
1. Add Student & Marks
2. View All Students
3. Calculate Average Marks
4. delete student
(press anything else to Exit)
        ''')
        choice = input("Enter your choice: ")
        if choice == '1':
            add_student(grades)
        elif choice == '2':
            view_students(grades)
        elif choice == '3':
            calculate_average(grades)
        elif choice == '4':
            delete_student(grades)
        else:
            print("Exiting Grade Manager. Goodbye!")
            print("Thank You! ")
            break

if __name__ == "__main__":
    grade_manager()
