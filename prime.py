#wap to input a number and check whether a number is prime or not
no=int(input("Enter the number to be checked:"))
if no<1:
    print("The given number is not prime")
else:
    for i in range(2,no):
        if no%i==0:print("The given number is not prime")
        break

    else:print("The given number is prime")
