#wap to check if a given number is a perfect number
no=int(input("Enter a number:"))
sum=0
for i in range(1,no):
    if no%i==0:
        sum=sum+i
if sum==no:print(f"{no} is a Perfect Number")
else:print(f"{no} is not a Perfect Number")
