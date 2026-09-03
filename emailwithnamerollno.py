#Take a student full name and rollno.Generate email using first 3 letters of first name,last name,and last 3 characters of rollno
first=input("Enter first name:")
last=input("Enter last name:")
roll=input("Enter rollno:")
email=first[0:3]+last[0:3]+roll[-3:]
print(email)
