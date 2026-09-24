#wap to store multiple student records as a list of tuples. Each tuple should contain name, roll number and marks. Display students who scored above 75.
students = [
    ("Radhika", 31, 85),
    ("Aman", 12, 72),
    ("Priya", 25, 91),
    ("Rahul", 18, 68),
    ("Neha", 20, 79)
]
print("Students who scored above 75:")
for student in students:
    if student[2] > 75:
        print(student)
