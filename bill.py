""" Wap to calculate the final bill amount after applying a discount The program should take the total bill amount as input from
 the user and apply the discount according to the following rules.
 After calculating the discount,the program should display the discount
 amount and the final bill"""
bill=float(input("Enter total bill amount:"))
if bill>5000:
    discount=bill*20/100
elif bill>=3000 and bill<=5000:
    discount=bill*10/100
else:
    discount=0
final_bill=bill-discount
print("Discount:",discount)
print("Final Bill:",final_bill)  
