#wap to input four numbers from the user and find the greatest number amongst them
n1=int(input("Enter number1:"))
n2=int(input("Enter number2:"))
n3=int(input("Enter number3:"))
n4=int(input("Enter number4:"))
if n1>n2 and n1>n3 and n1>n4:
    print("Number1 is greatest!")
elif n2>n1 and n2>n3 and n2>n4:
    print("Number2 is greatest!")
elif n3>n1 and n3>n2 and n3>n4:
    print("Number3 is greatest!")
else:print("Number 4 is greatest!")
