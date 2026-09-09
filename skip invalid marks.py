""" wap to input marks of 5 students 
For each student the program should check whether the entered marks are valid or invalid
If the marks are invalid it should skip those marks else should print all the valid marks """
for i in range(1,6):
    marks=int(input("Enter marks:"))
    if marks<0 or marks>100:
        print("Invalid marks skipped")
        continue
    print("Valid Marks:",marks)
