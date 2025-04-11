#     ✅ Assignment 1: Student Report Card Generator: Data Input and Grade Calculation System
# Program Description
# Objective: The program is designed to collect student data and generate report cards interactively. Users will input data for each student, and the program will compile this into a formatted report card, complete with grades based on the students' performance.

# Functionality
# Data Input: When the program starts, it prompts the user to enter the following details for a student:

# Student Name: [User inputs the student's name]
# Roll Number: [User inputs the student's roll number]
# Math: [User inputs marks obtained]
# Physics: [User inputs marks obtained]
# Urdu: [User inputs marks obtained]
# English: [User inputs marks obtained]
# Computer: [User inputs marks obtained] After the details for one student are entered, the program will display the message: "Record of [Student Name] inserted successfully. Do you want to insert more? Press 'Y' for Yes or 'N' for No."
# Continuation Logic: If the user presses 'Y', the program will prompt the entry of another student's data. If the user presses 'N', the program will terminate the input phase and proceed to generate the report cards.

# Report Generation:

# The program will display a list of all students whose data has been entered.
# For each student, a marksheet will be generated displaying the marks in each subject.
# The program calculates the total marks obtained and the percentage.
# Based on the percentage, the program assigns a grade according to the following scale:
# 40 to 49%: Grade F
# 50 to 59%: Grade C
# 60 to 69%: Grade B
# 70 to 79%: Grade A
# 80% and above: Grade A+
# Additional Features
# Error Handling: The program will include basic error handling to manage non-numeric input for marks and invalid choices (other than 'Y' or 'N').
# User Interface: A simple text-based interface will guide the user through the data entry and report viewing process.
# Flexibility: Users can input any number of students in a session, making the program suitable for batch processing at the end of program.



welcome = "Welcome to the Report Card Generator!"
print(welcome)


students_list = []

while True:
    student_data = {}
    student_data["student_name"] = input("Enter student name: ")
    student_data["student_roll_num"] = input("Enter student roll number: ")
    student_data["Math"] = input("Enter Math marks: ")
    student_data["Physics"] = input("Enter Physics marks: ")
    student_data["Urdu_Sindhi"] = input("Enter Urdu/Sindhi marks: ")
    student_data["English"] = input("Enter English marks: ")
    student_data["Computer_Biology"] = input("Enter Computer/Biology marks: ")
    student_data["Chemistry"] = input("Enter Chemistry marks: ")
    student_data["PST_Islamiat"] = input("Enter PST/Islamiat marks: ")
    print(f"Record of {student_data['student_name']} inserted successfully.")
    students_list.append(student_data.copy())
    cont = input("Do you want to insert more? Press 'Y' for Yes or 'N' for No. ")
    if cont.upper() == "N":
        break

for student in students_list:
    print("\nReport Card")
    print("Name:", student["student_name"])
    print("Roll Number:", student["student_roll_num"])

    math = int(student["Math"])
    physics = int(student["Physics"])
    urdu_sindhi = int(student["Urdu_Sindhi"])
    english = int(student["English"])
    computer_bio = int(student["Computer_Biology"])
    chemistry = int(student["Chemistry"])
    pst_islamiat = int(student["PST_Islamiat"])

    total = math + physics + urdu_sindhi + english + computer_bio + chemistry + pst_islamiat
    percentage = (total / 700) * 100

    if percentage >= 80:
        grade = "A+"
    elif percentage >= 70:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    elif percentage >= 40:
        grade = "F"
    else:
        grade = "Fail"

    print("Marks:")
    print(f"Math: {math}, Physics: {physics}, Urdu: {urdu_sindhi}, English: {english}, Computer/Biology: {computer_bio}, Chemistry: {chemistry}, PST/Islamiat: {pst_islamiat}")
    print("Total:", total)
    print("Percentage:", f"{percentage:.2f}%")
    print("Grade:", grade)