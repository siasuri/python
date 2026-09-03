'''
wap to determine whether a student is eligible for a scholarship the scholarship should be granted if the student satisfies either:
has a cgpa of 8.5 or above and attendance of 85 percent or above
the student has won a national level competition
'''
cgpa=float(input("Enter cgpa: "))
attendance=int(input("Enter attendance: "))
comp=input("Has won national level competition: ")
if cgpa>=8.5 and attendance>=85 or comp=="yes": print("Eligible")
else: print("Not Eligible")
