#wap to count how many times a particular element appears in the list
n=int(input("Enter the no of elements in the list:"))
list=[]
for i in range(n):
    num=int(input("Enter element:"))
    list.append(num)
 
search=int(input("Enter number to count:"))
count=0
for num in list:
  if num==search:
     count=count+1
print("Frequency:",count)
