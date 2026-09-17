"""1.Wap to input marks of n students in a list.Display highest marks,lowest marks,average marks,and number of students who passed"""
n=int(input("Enter no of students:"))
marks=[]
for i in range(0,n):
    m=int(input("Enter marks:"))
    marks.append(m)
highest=max(marks)
lowest=min(marks)
average=(sum(marks))/n
passed=0
for j in marks:
    if j>=40:
        passed+=1
print("Highest marks:",highest)
print("Lowest marks:",lowest)
print("Average:",average)
print("Number of students who passed:",passed)
