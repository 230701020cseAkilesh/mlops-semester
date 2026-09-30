

def calculate_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"


name = input("Enter student name: ")
mark = float(input("Enter marks: "))

grade = calculate_grade(mark)

print("\n--- Student Result ---")
print("Student:", name)
print("Marks:", mark)
print("Grade:", grade)
