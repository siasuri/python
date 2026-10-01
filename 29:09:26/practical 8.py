# Student database using list and tuples

n = int(input("Enter number of students: "))

database = []

for i in range(n):
    print("\nEnter details of student", i + 1)

    roll = int(input("Enter roll number: "))

    # Check unique roll number
    while True:
        exists = False

        for student in database:
            if student[0] == roll:
                exists = True
                break

        if exists:
            print("Roll number already exists!")
            roll = int(input("Enter another roll number: "))
        else:
            break

    name = input("Enter name: ")
    branch = input("Enter branch: ")
    cgpa = float(input("Enter CGPA: "))

    record = (roll, name, branch, cgpa)

    database.append(record)

print("\nAll Student Records:")

for student in database:
    print(student)

# Search using roll number
search_roll = int(input("\nEnter roll number to search: "))

found = False

for student in database:
    if student[0] == search_roll:
        print("\nStudent Found")
        print("Roll Number:", student[0])
        print("Name:", student[1])
        print("Branch:", student[2])
        print("CGPA:", student[3])
        found = True
        break

if not found:
    print("Student not found")
