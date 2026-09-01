"""Write a python program to take a student's full name and display:
Total number of characters 
First character
Last character
Name in uppercase form
"""
print("Enter student's full name:\n")
name=input(" ")
print("Total number of characters: ",len("name"))
print("First character: ",name[0])
print("Last character: ",name[-1])
print("Capitalized name= ",name.upper())

