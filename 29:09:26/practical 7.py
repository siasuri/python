# Student records using list and dictionary

n = int(input("Enter number of students: "))

students = []

for i in range(n):
    print("\nEnter details of student", i + 1)

    roll = int(input("Enter roll number: "))

    # Check unique roll number
    while True:
        exists = False

        for student in students:
            if student["roll"] == roll:
                exists = True
                break

        if exists:
            print("Roll number already exists!")
            roll = int(input("Enter another roll number: "))
        else:
            break

    name = input("Enter name: ")
    branch = input("Enter branch: ")
    marks = float(input("Enter marks: "))

    student = {
        "roll": roll,
        "name": name,
        "branch": branch,
        "marks": marks
    }

    students.append(student)

print("\nAll Student Records:")

for student in students:
    print(student)

# Search student
search_roll = int(input("\nEnter roll number to search: "))

found = False

for student in students:
    if student["roll"] == search_roll:
        print("\nStudent Found")
        print("Roll Number:", student["roll"])
        print("Name:", student["name"])
        print("Branch:", student["branch"])
        print("Marks:", student["marks"])
        found = True
        break

if not found:
    print("Student not found")
