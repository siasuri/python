numbers=(10,20,30,40)
print("Original tuple:",numbers)
temp=list(numbers)
temp[1]=200
numbers=tuple(temp)
print("Updated tuple:",numbers)
