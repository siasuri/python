#wap to input a number and reverse using arithmetic operations only
no=int(input("Enter a number:"))
rev=0
while no>0:
    digit=no%10
    rev=rev*10+digit
    no=no//10
print("Reverse:",rev)
