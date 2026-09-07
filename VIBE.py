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

    def __init__(self, name, student_id, test1=0, test2=0, test3=0):
        self.name = name
        self.id = student_id
        self.Test1 = float(test1)
        self.Test2 = float(test2)
        self.Test3 = float(test3)
        self.average = self.calculate_average()
        self.grade = self.calculate_letter_grade()

    def calculate_average(self):
        """Return this student's average score as a float."""
        return (self.Test1 + self.Test2 + self.Test3) / 3

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

    def update_grade(self):
        """Recalculate this student's average and letter grade."""
        self.average = self.calculate_average()
        self.grade = self.calculate_letter_grade()

    def __str__(self):
        """Return a formatted summary of this student's record."""
        return (
            f"Name: {self.name} | ID: {self.id} | "
            f"Test1: {self.Test1:.2f} | Test2: {self.Test2:.2f} | "
            f"Test3: {self.Test3:.2f} | Average: {self.average:.2f} | "
            f"Grade: {self.grade}"
        )


def get_score(test_name):
    """Prompt for a valid score from 0 through 100."""
    while True:
        try:
            score = float(input(f"Enter {test_name} score (0-100): "))
            if 0 <= score <= 100:
                return score
            print("Score must be between 0 and 100.")
        except ValueError:
            print("Please enter a numeric score.")


def add_new_student_record(students):
    """Prompt for and add one Student object to the records list."""
    name = input("Enter student name: ").strip()
    if not name:
        print("Student name cannot be blank.")
        return

    student_id = input("Enter student ID: ").strip()
    if not student_id:
        print("Student ID cannot be blank.")
        return

    new_student = Student(name, student_id)
    new_student.Test1 = get_score("Test1")
    new_student.Test2 = get_score("Test2")
    new_student.Test3 = get_score("Test3")
    new_student.update_grade()
    for index, student in enumerate(students):
        if student.id == student_id:
            students[index] = new_student
            print(f"Record updated:\n{new_student}")
            return
    students.append(new_student)
    print(f"Record saved:\n{new_student}")


def load_student_records():
    """Load Student objects from the pipe-delimited records file."""
    students = []
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            for line in file:
                fields = line.rstrip("\n").split("|")
                if len(fields) not in (5, 7):
                    continue
                try:
                    student = Student(*fields[:5])
                    if len(fields) == 7:
                        student.average = float(fields[5])
                        student.grade = fields[6]
                    students.append(student)
                except ValueError:
                    continue
    except FileNotFoundError:
        print(f"No existing {FILE_NAME} found. Starting with no records.")
    except (OSError, UnicodeError) as error:
        print(f"Could not load {FILE_NAME}: {error}")
    return students


def save_student_records(students):
    """Save Student objects as pipe-delimited text records."""
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            for student in students:
                file.write(
                    f"{student.name}|{student.id}|{student.Test1:.2f}|"
                    f"{student.Test2:.2f}|{student.Test3:.2f}|"
                    f"{student.average:.2f}|"
                    f"{student.grade}\n"
                )
    except (OSError, UnicodeError) as error:
        print(f"Could not save {FILE_NAME}: {error}")
        return False
    print(f"Saved {len(students)} student record(s) to {FILE_NAME}.")
    return True


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


def display_class_statistics(students):
    """Display highest, lowest, and overall class averages."""
    if not students:
        print("No student records found.")
        return

    averages = [student.average for student in students]
    print("\nClass Statistics")
    print(f"Highest average: {max(averages):.2f}")
    print(f"Lowest average:  {min(averages):.2f}")
    print(f"Class average:   {sum(averages) / len(averages):.2f}")


def search_student(students):
    """Find and display students whose names contain the search text."""
    search_name = input("Enter student name to search: ").strip().lower()
    matches = [student for student in students if search_name in student.name.lower()]
    if not matches:
        print("No matching student found.")
        return

    for student in matches:
        print(student)


def display_menu_instruction(choice):
    """Display only the instruction for the selected menu item."""
    if choice == "1":
        print("Enter a name, student ID, and three scores from 0 to 100.")
        print("The average and letter grade are calculated automatically.")
        print("Grades: A = 90-100, B = 80-89, C = 70-79, D = 60-69, F < 60.")
    elif choice == "2":
        print("Displays every student in a table with scores, average, and grade.")
    elif choice == "3":
        print("Enter all or part of a name. The search is case-insensitive.")
    elif choice == "4":
        print("Displays the highest, lowest, and overall class averages.")
    elif choice == "5":
        print("Saves all records to student_grades.txt in pipe-delimited format.")
    elif choice == "6":
        print("Opens the usage-instructions submenu for the program.")
    elif choice == "e":
        print("Records are saved automatically before the program exits.")


def display_usage_instructions():
    """Display a submenu for selecting one usage instruction."""
    while True:
        print("\nUsage Instructions")
        print("1. Add new student record")
        print("2. Display all students")
        print("3. Search for student by name")
        print("4. Display class statistics")
        print("5. Save student records")
        print("6. Display usage instructions")
        print("E. Exit")
        print("B. Return to main menu")
        choice = input("Choose a menu item for instructions: ").strip().lower()

        if choice in ("1", "2", "3", "4", "5", "6"):
            display_menu_instruction(choice)
        elif choice == "e":
            display_menu_instruction(choice)
        elif choice in ("b", ""):
            return
        else:
            print("Invalid usage menu choice. Select 1 through 6 or B.")


def main():
    """Run the Student Grade Calculator menu."""
    students = load_student_records()
    print(f"Loaded {len(students)} student record(s) from {FILE_NAME}.")
    print("For instructions about a menu option, select option 7.")

    while True:
        print("\nStudent Grade Calculator")
        print("1. Add new student record")
        print("2. Display all students")
        print("3. Search for student by name")
        print("4. Display class statistics")
        print("5. Save student records")
        print("6. Display usage instructions")
        print("Press ESC to save and exit")
        choice = input("Choose an option: ").strip()

        if choice in ("\x1b", "ESC", "esc"):
            display_menu_instruction("e")
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
            display_usage_instructions()
        else:
            print("Invalid choice. Please select a menu option.")


if __name__ == "__main__":
    main()
