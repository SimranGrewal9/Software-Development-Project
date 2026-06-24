"Student Management System using Python"
class Student:
    """Class to store student details."""

    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks
def add_student(student_list):
    """Add a new student."""

    name = input("Enter student name: ")
    roll_number = input("Enter roll number: ")
    marks = input("Enter marks: ")

    student = Student(name, roll_number, marks)
    student_list.append(student)

    print("Student added successfully.")
def view_students(student_list):
    """Display all students."""

    if not student_list:
        print("No records found.")
        return

    for student in student_list:
        print("\nName:", student.name)
        print("Roll Number:", student.roll_number)
        print("Marks:", student.marks)
def save_to_file(student_list):
    """Save student data to file."""

    with open("students.txt", "w") as file:
        for student in student_list:
            file.write(
                f"{student.name}, "
                f"{student.roll_number}, "
                f"{student.marks}\n"
            )

    print("Data saved successfully.")
def main():
    """Main menu."""

    student_list = []

    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Save to File")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student(student_list)

        elif choice == "2":
            view_students(student_list)

        elif choice == "3":
            save_to_file(student_list)

        elif choice == "4":
            print("Program exited.")
            break

        else:
            print("Invalid choice.")
if __name__ == "__main__":
    main()
	
OUTPUT:

1. Add Student
2. View Students
3. Save to File
4. Exit
Enter choice:  1
Enter student name:  Sam
Enter roll number:  102
Enter marks:  92
Student added successfully.

1. Add Student
2. View Students
3. Save to File
4. Exit
Enter choice:  2

Name: Sam
Roll Number: 102
Marks: 92

1. Add Student
2. View Students
3. Save to File
4. Exit
Enter choice:  3
Data saved successfully.

1. Add Student
2. View Students
3. Save to File
4. Exit
Click to add a cell.