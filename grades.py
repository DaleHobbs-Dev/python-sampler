"""
Simple module to manage student grades.
"""

# Initialize an empty dictionary to store student grades
student_grades = {}


# Function to add a student's grade
def add_grade(student, grade):
    """Add the grade for a student."""
    student = student.lower()
    if student in student_grades:
        del student_grades[student]
        student_grades[student] = int(grade)
        print(f"Grade `{grade}` updated for student `{student}`")
    else:
        student_grades[student] = grade
        print(f"Grade '{grade}' added for student '{student}'.")


# Function to remove a student's grade
def remove_grade(student):
    """Remove the grade for a student."""
    student = student.lower()
    if student in student_grades:
        del student_grades[student]
        print(f"Grade removed for student '{student}'.")
    else:
        print(f"Student '{student}' not found.")


# Function to display all students as well as their grades
def display_grades():
    """Display all students and their grades"""
    for s, g in student_grades.items():
        print(f"{s}: {g}")


# Function to update a student's grade
def update_grade(name, grade):
    """Update grade for a student"""
    name = name.lower()
    if name in student_grades:
        add_grade(name, grade)
    else:
        print(f"{name} hasn't been added to the gradebook yet and cannot be updated")


# Find the grade for a student
def find_grade(name):
    """Find a student in the gradebook"""
    name = name.lower()
    if name in student_grades:
        grade = student_grades[name]
        print(f"{name}'s current grade is {grade}.")
    else:
        print(f"{name} was not found inside the gradebook")


# Function used to calculate the class average
def average_grades():
    """Calculate the class's average"""
    total = sum(grade for grade in student_grades.values())
    average = total / len(student_grades)
    print(f"the class average for grades in the gradebook is {average}")


# Adding some grades
add_grade("Alice", "98")
add_grade("Blake", "74")
add_grade("Patty", "63")

# Displaying some grades
display_grades()

# Updating some Grades
add_grade("Alice", "94")
update_grade("Patty", "84")
update_grade("Marcus", "99")

# Removing a grade
remove_grade("Blake")

# Finding a Grade
find_grade("Blake")
find_grade("aLiCe")

# Average the grades
average_grades()

# Display grades again
display_grades()
