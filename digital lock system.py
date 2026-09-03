""" wap to simulate a digital lock system the lock should ask the user to enter a 4 digit PIN if the entered Pin does not contain exactly 4 digits,the program should display an error message and ask again if the entered PIN is correct the lock should open otherwise try again"""
pin=input("Enter PIN: ")
if(len(pin)==4 and pin==1234): print("Lock Open!!")
else:print("Try again!!")
