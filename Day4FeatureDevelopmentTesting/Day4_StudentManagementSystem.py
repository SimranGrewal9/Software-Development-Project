import csv
import os

FILE_NAME = "students.csv"

# Create CSV file if it does not exist
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Marks"])

# Add Student
def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    marks = input("Enter Student Marks: ")

    # Input Validation
    if student_id == "" or name == "" or marks == "":
        print("Error: All fields are required.")
        return

    if not marks.isdigit():
        print("Error: Marks must be numeric.")
        return

    # Check duplicate ID
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == student_id:
                print("Error: Student ID already exists.")
                return

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([student_id, name, marks])

    print("Student added successfully.")

# Display Students
def display_students():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        print("\nStudent Records:")
        for row in reader:
            print(row)

# Search Student
def search_student():
    search_id = input("Enter Student ID to search: ")

    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0] == search_id:
                print("Student Found:", row)
                found = True

    if not found:
        print("Student not found.")

# Update Student
def update_student():
    search_id = input("Enter Student ID to update: ")

    updated_data = []
    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0] == search_id:
                found = True

                new_name = input("Enter New Name: ")
                new_marks = input("Enter New Marks: ")

                if not new_marks.isdigit():
                    print("Error: Marks must be numeric.")
                    return

                updated_data.append([search_id, new_name, new_marks])

            else:
                updated_data.append(row)

    if found:
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(updated_data)

        print("Student updated successfully.")

    else:
        print("Student not found.")

# Delete Student
def delete_student():
    search_id = input("Enter Student ID to delete: ")

    updated_data = []
    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0] == search_id:
                found = True
            else:
                updated_data.append(row)

    if found:
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(updated_data)

        print("Student deleted successfully.")

    else:
        print("Student not found.")

# Main Program
while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Program exited.")
        break

    else:
        print("Invalid choice.")

OUTPUT:
===== Student Management System =====
1. Add Student
2. Display Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
Enter your choice:  1
Enter Student ID:  2
Enter Student Name:  ENA
Enter Student Marks:  45
Student added successfully.

===== Student Management System =====
1. Add Student
2. Display Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
Enter your choice:  1
Enter Student ID:  
Enter Student Name:  
Enter Student Marks:  
Error: All fields are required.

===== Student Management System =====
1. Add Student
2. Display Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
Enter your choice:  1
Enter Student ID:  3
Enter Student Name:  ANA
Enter Student Marks:  R
Error: Marks must be numeric.

===== Student Management System =====
1. Add Student
2. Display Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
Enter your choice:  3
Enter Student ID to search:  2
Student Found: ['2', 'ENA', '45']

===== Student Management System =====
1. Add Student
2. Display Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
Enter your choice:  3
Enter Student ID to search:  7
Student not found.

===== Student Management System =====
1. Add Student
2. Display Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
Enter your choice:  4
Enter Student ID to update:  2
Enter New Name:  SITA
Enter New Marks:  89
Student updated successfully.

===== Student Management System =====
1. Add Student
2. Display Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
Enter your choice:  5
Enter Student ID to delete:  3
Student not found.

===== Student Management System =====
1. Add Student
2. Display Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
Enter your choice:  5
Enter Student ID to delete:  2
Student deleted successfully.

===== Student Management System =====
1. Add Student
2. Display Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
