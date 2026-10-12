print("Welcome to the Student Data Organizer!")

students = {}

while True:
    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == "1":
        print("\nEnter student details:")

        student_id = input("Student ID: ")
        name = input("Name: ")
        age = int(input("Age: "))
        grade = input("Grade: ")
        dob = input("Date of Birth (YYYY-MM-DD): ")
        subjects = input("Subjects (comma-separated): ")

        students[student_id] = {
            "name": name,
            "age": age,
            "grade": grade,
            "dob": dob,
            "subjects": subjects
        }

        print("\nStudent added successfully!")

    # Display All Students
    elif choice == "2":
        print("\n--- Display All Students ---")

        if len(students) == 0:
            print("No students found.")
        else:
            for student_id, student in students.items():
                print(
                    f"Student ID: {student_id} | "
                    f"Name: {student['name']} | "
                    f"Age: {student['age']} | "
                    f"Grade: {student['grade']} | "
                    f"Subjects: {student['subjects']}"
                )

    # Update Student
    elif choice == "3":
        print("\n--- Update Student Information ---")

        student_id = input("Enter Student ID: ")

        if student_id in students:
            print("Enter new details:")

            students[student_id]["name"] = input("Name: ")
            students[student_id]["age"] = int(input("Age: "))
            students[student_id]["grade"] = input("Grade: ")
            students[student_id]["dob"] = input(
                "Date of Birth (YYYY-MM-DD): "
            )
            students[student_id]["subjects"] = input(
                "Subjects (comma-separated): "
            )

            print("\nStudent information updated successfully!")
        else:
            print("Student not found!")

    # Delete Student
    elif choice == "4":
        print("\n--- Delete Student ---")

        student_id = input("Enter Student ID: ")

        if student_id in students:
            del students[student_id]
            print("Student deleted successfully!")
        else:
            print("Student not found!")

    # Display Subjects
    elif choice == "5":
        print("\n--- Subjects Offered ---")

        subjects = [
            "Math",
            "Science",
            "English",
            "Computer Science",
            "Social Science"
        ]

        for subject in subjects:
            print(subject)

    # Exit
    elif choice == "6":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 6.")