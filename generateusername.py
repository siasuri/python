"""WAP to take a student name and roll number then generate a username 
 using the first 3 letters of the name and the last 2 digits of the rollnumber"""
print("Enter student name:")
name=input(" ")
print("Enter rollnumber:")
rollno=input(" ")
username=name[:3] +rollno[-2:]
print("Generated username: ",username)
