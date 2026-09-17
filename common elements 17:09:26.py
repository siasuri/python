list1=[10,20,30,40]
list2=[10,20,90,7]
common=[]
num=int(input("Enter number:"))
for num in list1:
    if num in list2 and num not in common:
        common.append(num)
print("First list:",list1)
print("Second list:",list2)
print("Common Elements:",common)
