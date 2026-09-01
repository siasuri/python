#wap to take a 10 digit mobile number and displayonly the last 4 digits 
mobile=input("Enter mobile number: ")
masked="******"+mobile[-4:]
print("Masked mobile number: ",masked)
