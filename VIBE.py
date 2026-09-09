#James Smidt
#CIS261
#WK10 VIBE Coding


"""Student Grade Calculator.

Program purpose: manage student records, test scores, and calculated grades.
Data structure choice: Option B, using a Student class.
"""


FILE_NAME = "student_grades.txt"


class Student:
    """Store one student's information and calculated grade."""

    # Create a student record with a name, ID, and three test scores.
    def __init__(self, name, student_id, test1=0, test2=0, test3=0):
        self.name = name
        self.id = student_id
        self.Test1 = float(test1)
        self.Test2 = float(test2)
        self.Test3 = float(test3)
        self.average = self.calculate_average()
        self.grade = self.calculate_letter_grade()

    # Calculate the student's average score across all three tests.
    def calculate_average(self):
        """Return this student's average score as a float."""
        return (self.Test1 + self.Test2 + self.Test3) / 3

    # Convert the student's numeric average into a letter grade.
    def calculate_letter_grade(self):
        """Return this student's letter grade based on the average."""
        if self.average >= 90:
            return "A"
        if self.average >= 80:
            return "B"
        if self.average >= 70:
            return "C"
        if self.average >= 60:
            return "D"
        return "F"

    # Refresh the calculated average and letter grade after score changes.
    def update_grade(self):
        """Recalculate this student's average and letter grade."""
        self.average = self.calculate_average()
        self.grade = self.calculate_letter_grade()

    # Format the student's details into a readable summary for display.
    def __str__(self):
        """Return a human-readable summary of this student's record."""
        return (
            f"Name: {self.name}\n"
            f"ID: {self.id}\n"
            f"Test 1: {self.Test1:.2f}\n"
            f"Test 2: {self.Test2:.2f}\n"
            f"Test 3: {self.Test3:.2f}\n"
            f"Average: {self.average:.2f}\n"
            f"Letter Grade: {self.grade}"
        )

    # Prepare the student record for saving in the text file format.
    def to_file_string(self):
        """Return this student's record in pipe-delimited file format."""
        return (
            f"{self.name}|{self.id}|{self.Test1:.2f}|"
            f"{self.Test2:.2f}|{self.Test3:.2f}|"
            f"{self.average:.2f}|{self.grade}"
        )


# Ask the user for a test score and keep prompting until it is valid.
def get_score(test_name):
    """Prompt for a valid score from 0 through 100."""
    while True:
        try:
            score_text = input(f"Enter {test_name} score (0-100), or ESC to stop: ")
            if score_text.strip().lower() in ("esc", "\x1b"):
                return None
            score = float(score_text)
            if 0 <= score <= 100:
                return score
            print("Score must be between 0 and 100.")
        except ValueError:
            print("Please enter a numeric score.")


# Collect a student's name, ID, and scores and add or update the record.
def add_new_student_record(students):
    """Prompt for and add students until ESC is entered."""
    while True:
        name = input("\nEnter student name, or ESC to stop adding: ").strip()
        if name.lower() in ("esc", "\x1b"):
            save_student_records(students)
            print("Returning to the main menu.")
            return
        if not name:
            print("Student name cannot be blank.")
            continue

        student_id = input("Enter student ID, or ESC to stop adding: ").strip()
        if student_id.lower() in ("esc", "\x1b"):
            save_student_records(students)
            print("Returning to the main menu.")
            return
        if not student_id:
            print("Student ID cannot be blank.")
            continue

        test1 = get_score("Test1")
        if test1 is None:
            save_student_records(students)
            print("Returning to the main menu.")
            return
        test2 = get_score("Test2")
        if test2 is None:
            save_student_records(students)
            print("Returning to the main menu.")
            return
        test3 = get_score("Test3")
        if test3 is None:
            save_student_records(students)
            print("Returning to the main menu.")
            return

        new_student = Student(name, student_id, test1, test2, test3)
        record_summary = (
            f"Name: {new_student.name}, ID: {new_student.id}\n"
            f"Average: {new_student.average:.2f}, "
            f"Letter Grade: {new_student.grade}"
        )
        for index, student in enumerate(students):
            if student.id == student_id:
                students[index] = new_student
                print("Record updated:")
                print(record_summary)
                break
        else:
            students.append(new_student)
            print("Record saved:")
            print(record_summary)


# Read all saved student records from the file and recreate Student objects.
def load_student_records():
    """Load Student objects from the pipe-delimited records file."""
    students = []
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            for line in file:
                fields = line.rstrip("\n").split("|")
                if len(fields) != 7:
                    continue
                try:
                    student = Student(*fields[:5])
                    student.average = float(fields[5])
                    student.grade = fields[6]
                    students.append(student)
                except ValueError:
                    continue
    except FileNotFoundError:
        print(f"No existing {FILE_NAME} found. Starting with no records.")
    except (OSError, UnicodeError) as error:
        print(f"Could not load {FILE_NAME}: {error}")
    except Exception as error:
        print(f"Could not load {FILE_NAME}: {error}")
    return students


# Write every student record to the data file so it can be restored later.
def save_student_records(students):
    """Save Student objects as pipe-delimited text records."""
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            for student in students:
                file.write(student.to_file_string() + "\n")
    except (OSError, UnicodeError) as error:
        print(f"Could not save {FILE_NAME}: {error}")
        return False
    except Exception as error:
        print(f"Could not save {FILE_NAME}: {error}")
        return False
    print(f"Saved {len(students)} student record(s) to {FILE_NAME}.")
    return True


# Show all students in a table with their scores, average, and grade.
def display_students(students):
    """Display all student records in a formatted table."""
    if not students:
        print("No student records found.")
        return

    print("\nStudent Grade Report")
    print("-" * 91)
    print(
        f"{'Name':<20} {'Student ID':<15} {'Test1':>7} "
        f"{'Test2':>7} {'Test3':>7} {'Average':>9} {'Grade':>7}"
    )
    print("-" * 91)
    for student in students:
        print(
            f"{student.name[:20]:<20} {student.id[:15]:<15} "
            f"{student.Test1:>7.2f} {student.Test2:>7.2f} "
            f"{student.Test3:>7.2f} {student.average:>9.2f} "
            f"{student.grade:>7}"
        )
    print("-" * 91)
    input("Press Enter to return to the main menu.")


# Display the highest, lowest, and overall average for the class.
def display_class_statistics(students):
    """Display highest, lowest, and overall class averages."""
    if not students:
        print("No student records found.")
        input("Press Enter to return to the main menu.")
        return

    averages = [student.average for student in students]
    print("\nClass Statistics")
    print(f"Highest average: {max(averages):.2f}")
    print(f"Lowest average:  {min(averages):.2f}")
    print(f"Class average:   {sum(averages) / len(averages):.2f}")
    input("Press Enter to return to the main menu.")


# Search the list by name and let the user look up more students if needed.
def search_student(students):
    """Search for students and repeat while the user chooses to continue."""
    while True:
        search_name = input("Enter student name to search: ").strip().lower()
        matches = [
            student for student in students if search_name in student.name.lower()
        ]
        if not matches:
            print("No matching student found.")
        else:
            for student in matches:
                print(student)

        while True:
            search_again = input("Search for another student? (Yes/No): ").strip().lower()
            if search_again in ("y", "yes"):
                break
            if search_again in ("n", "no"):
                input("Press Enter to return to the main menu.")
                return
            print("Please enter Yes or No.")


# Show the help text for the selected menu option.
def display_menu_instruction(choice):
    """Display only the instruction for the selected menu item."""
    print("\n" + "-" * 58)
    print("Menu Instructions".center(58))
    print("-" * 58)
    if choice == "1":
        print("Add New Student Records")
        print("  Enter a name, student ID, and three scores from 0 to 100.")
        print("  The average and letter grade are calculated automatically.")
        print("  Continue entering students until you type ESC.")
        print("  Grades: A = 90-100, B = 80-89, C = 70-79,")
        print("          D = 60-69, and F = below 60.")
    elif choice == "2":
        print("Display All Students")
        print("  Displays every student in a table with scores, average, and grade.")
    elif choice == "3":
        print("Search for Student by Name")
        print("  Enter all or part of a name.")
        print("  The search is case-insensitive.")
    elif choice == "4":
        print("Display Class Statistics")
        print("  Displays the highest, lowest, and overall class averages.")
    elif choice == "5":
        print("Save Student Records")
        print("  Saves all records to student_grades.txt")
        print("  in pipe-delimited format.")
    elif choice == "6":
        print("Display Usage Instructions")
        print("  Opens the usage-instructions submenu for the program.")
    elif choice == "7":
        print("Exit")
        print("  Saves all records and exits the program.")
    print("-" * 58)


# Present a submenu explaining what each program option does.
def display_usage_instructions():
    """Display a submenu for selecting one usage instruction."""
    while True:
        print("\n" + "=" * 58)
        print("Usage Instructions".center(58))
        print("=" * 58)
        print("1.  Add new student record")
        print("2.  Display all students")
        print("3.  Search for student by name")
        print("4.  Display class statistics")
        print("5.  Save student records")
        print("6.  Display usage instructions")
        print("7.  Exit")
        print("B.  Return to main menu")
        print("-" * 58)
        choice = input("Choose a menu item for instructions: ").strip().lower()

        if choice in ("\x1b", "esc", "7"):
            return True
        if choice in ("1", "2", "3", "4", "5", "6", "7"):
            display_menu_instruction(choice)
        elif choice in ("b", ""):
            return False
        else:
            print("Invalid usage menu choice. Select 1 through 7 or B.")


# Run the main menu loop for the student grade calculator.
def main():
    """Run the Student Grade Calculator menu."""
    students = load_student_records()
    print(f"Loaded {len(students)} student record(s) from {FILE_NAME}.")
    print("For instructions about a menu option, select option 6.")

    while True:
        print("\n" + "=" * 58)
        print("Student Grade Calculator".center(58))
        print("=" * 58)
        print("1.  Add new student record")
        print("2.  Display all students")
        print("3.  Search for student by name")
        print("4.  Display class statistics")
        print("5.  Save student records")
        print("6.  Display usage instructions")
        print("7.  Exit")
        print("-" * 58)
        print("Press ESC, type ESC, or enter 7 to save and exit.")
        print("=" * 58)
        choice = input("Choose an option: ").strip()

        if choice in ("\x1b", "ESC", "esc", "7"):
            save_student_records(students)
            print("Goodbye!")
            break
        if choice == "1":
            display_menu_instruction(choice)
            add_new_student_record(students)
        elif choice == "2":
            display_menu_instruction(choice)
            display_students(students)
        elif choice == "3":
            display_menu_instruction(choice)
            search_student(students)
        elif choice == "4":
            display_menu_instruction(choice)
            display_class_statistics(students)
        elif choice == "5":
            display_menu_instruction(choice)
            save_student_records(students)
        elif choice == "6":
            if display_usage_instructions():
                save_student_records(students)
                print("Goodbye!")
                break
        else:
            print("Invalid choice. Please select a menu option.")


if __name__ == "__main__":
    main()
