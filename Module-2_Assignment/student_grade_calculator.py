def calculate_grade(average):
    if average >= 80:
        return "A+"
    elif average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "F"


# Take student name
student_name = input("Enter Student Name: ")

# Take marks for 3 subjects
total_marks = 0

for i in range(1, 4):
    marks = float(input(f"Enter marks for Subject {i}: "))
    total_marks = total_marks + marks

# Calculate average
average = total_marks / 3

# Calculate grade
grade = calculate_grade(average)

# Display result
print("\n========== Student Result ==========")
print(f"Student Name: {student_name}")
print(f"Total Marks: {int(total_marks):}")
print(f"Average: {average:.2f}")
print(f"Grade: {grade}")
print("====================================")
