grades = []
student_count = int(input("Enter number of students: "))

def gradeTracker():
    for i in range(student_count):
        while True:
            try:
                marks = int(input(f"Enter marks for student {i+1}: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        if marks >= 80:
            print("Grade A")
        elif marks >= 60:
            print("Grade B")
        elif marks >= 40:
            print("Grade C")
        else:
            print("Grade D")
        grades.append(marks)

    print("All Grades:", grades)

def avg():
    print("Average Marks:", sum(grades) / student_count)

def highest_marks():
    print("Highest Marks: ", max(grades))

def lowest_marks():
    print("Lowest Marks:", min(grades))


gradeTracker()
avg()
highest_marks()
lowest_marks()
