#wap to take rollno like 2024A1R057 and extract admission year,program code, and rollno digits using slicing
roll=input("Enter rollno: ")
admission=roll[0:4]
code=roll[4:6]
digits=roll[6:]
print("admission year:",admission)
print("code: ",code)
print("rollno digits:",digits)
