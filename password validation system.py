""" Wap to create a simple password and validation system
The program should repeatedly ask the user to enter a password untill a valid password is entered.A password
will be considered valid only if it has at least 8 characters and contains the @ symbol,
Once the user enters a valid password the program should display "Password accepted" and stop Otherwise it should "Weak password Try ahgain later and ask for password again"""
while True:
    password = input("Enter your password: ")

    if len(password) >= 8 and "@" in password:
        print("Password accepted")
        break
    else:
        print("Weak password. Try again later.")
