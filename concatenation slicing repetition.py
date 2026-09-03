student_name=input("Enter student name: ")
branch=input("Enter branch name: ")
year=input("Enter year: ")
code_name=student_name[:3]+"-"+branch[:3]+"-"+year[-2:]
print("*" *30)
print("Student Code: ",code_name)
print("*" *30)
