#Write a python code to take marks of 3 subject =s and print true if marks in all 3 subjects are atleast 40 and avg marks is atleast 50
print("Enter marks of subject 1:")
m1=int(input(" "))
print("Enter marks of subject 2:")
m2=int(input(" "))
print("Enter marks of subject 3:")
m3=int(input(" "))
avg=(m1+m2+m3)/3
if m1>=40 and m2>=40 and m3>=40 and avg>=50:
    print("True")
else: print("False")