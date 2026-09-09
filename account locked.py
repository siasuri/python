#wap that asks the user to enter a username and password.The user should get only 3 attempts.If the correct credententials are entered, display "Logic Successfully" and stop the loop.If all attempts are used,display "Account Locked"
correct_username="Admin"
correct_password="python123"
attempts=3
while attempts>0:
    username=input("Enter username:")
    password=input("Enter password:")
    if username==correct_username and password==correct_password:
        print("Login Successful")
        break
    else:
        attempts=attempts-1
        print("Wrong details.Attempts left:",attempts)
    if attempts==0:
        print("Account locked")
