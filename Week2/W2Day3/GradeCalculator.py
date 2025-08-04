def gradeCalculatorfromMarks():
    marks = int(input("Enter your marks:"))
    if marks >= 80:
        print("Grade A")
    elif marks >= 60:
        print("Grade B")
    elif marks >= 40:
        print("Grade C")
    elif marks>=35:
        print("Grade D")
    else:
        print("Fail")
gradeCalculatorfromMarks()