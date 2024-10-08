status = True
grades = [67, 95, 88, 42, 99, 77]
lgrades = []
x = 0
global choice

def show_menu():
    global choice
    print("Welcome to my grading system.")
    print("Press 1 to view grades")
    print("Press 2 to add grades")
    print("Press 3 to remove grades")
    print("Press 4 to convert to letter grades")
    print("Press 5 to exit the program")
    choice = int(input("Enter your choice: "))

def show_grades():
    for grade in grades:
        print(grade)

def add_grades():
    new_grade = int(input("Enter your new grade: "))
    grades.append(new_grade)
    print("You added the grade " + str(new_grade) + " to your list")

def remove_grades():
    delete_grade = int(input("Which index would you like to delete?"))
    if delete_grade == -1:
        print("You deleted the grade: " + str(grades.pop()))
    else:
        print("You deleted the grade: " + str(grades.pop(delete_grade)))

def convert_letter_grades():
    lgrades = []
    for x in range(len(grades)):
        if grades[x] >= 90:
            lgrades.insert(x, "A")
        elif grades[x] >= 80:
            lgrades.insert(x, "B")
        elif grades[x] >= 70:
            lgrades.insert(x, "C")
        elif grades[x] >= 60:
            lgrades.insert(x, "D")
        else:
            lgrades.insert(x, "F")
    print(grades)
    print(lgrades)
while(status):
    show_menu()
    if choice ==1:
        show_grades()
    elif choice ==2:
        add_grades()
    elif choice ==3:
        print("The following are your grades.  If you wish to simply delete the last one, enter -1")
        show_grades()
    elif choice ==4:
        convert_letter_grades()
    elif choice ==5:
        print("Thank you for using our program.  Have a great day!")
        status = False
    else:
        print("Please read the menu carefully and select a valid option.")