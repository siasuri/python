#wap to take an email address and print the domain name
print("Enter email address:")
email=input(" ")
index=email.find("@")
domain=email[index+1:]
print("Domain: ",domain)
