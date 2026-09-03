#Take a password and check length,presence of @ and whether first and last characters are different
password=input("Enter password: ")
print("Length:",len(password))
print("@"in password)
first=password[0]
last=password[-1]
print(first!=last)
