# CIS261_WK10_VIBE
CIS 261 VIBE Coding Week 10 Assignment

## Student Grade Calculator

### Starting the Program

Run the program from the project folder:

```text
python VIBE.py
```

When the program starts, it automatically loads existing records from
`student_grades.txt`. If the file does not exist, the program starts with an
empty student list.

### Main Menu

Choose a menu option by entering its number and pressing Enter.

1. **Add new student record**
	- Enter the student's name as text.
	- Enter the student's ID as text.
	- Enter `Test1`, `Test2`, and `Test3` as scores from `0` through `100`.
	- The program calculates the average and letter grade automatically.
	- If the ID already exists, the existing record is updated.
	- Continue entering students until you type `ESC`.

2. **Display all students**
	- Shows every student in a formatted table.
	- The table includes the name, ID, three test scores, average, and letter
	  grade.

3. **Search for student by name**
	- Enter all or part of a student's name.
	- The search is case-insensitive. For example, `alice` finds `Alice Smith`.
	- Matching student details are displayed using the formatted student record.

4. **Display class statistics**
	- Shows the highest student average.
	- Shows the lowest student average.
	- Shows the overall class average.

5. **Save student records**
	- Saves all current records to `student_grades.txt`.
	- Records use this pipe-delimited format:

	  ```text
	  name|id|test1|test2|test3|average|grade
	  ```

6. **Display usage instructions**
	- Opens a submenu where you can select one menu item to view its instructions.
	- Enter `B` to return to the main menu.

**Exit (ESC or 7)**
	- Press the Escape key, enter `ESC` or `esc`, or enter `7` to exit.
	- The program automatically saves all records before exiting.

### Input Rules

- Names and IDs cannot be blank.
- Test scores must be numeric values between `0` and `100`.
- Invalid scores or menu choices display an error message and allow you to try
  again.
- Letter grades use the following scale: A = 90-100, B = 80-89, C = 70-79,
  D = 60-69, and F = below 60.
