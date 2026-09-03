#Take a student full name and rollno.Generate email using first 3 letters of first name,last name,rollno
first=input("")
last=input("")
roll=int(input(""))
email=first[0:3]+last[0:3]+roll[0:3]
print(email)
