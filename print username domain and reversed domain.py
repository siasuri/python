#wap to take an email address and print username domain and reversed domain
email=input("Enter email: ")
at=email.find("@")
username=email[:at]
domain=email[at+1:]
reverse=domain[::-1]
print(f"username:{username}\ndomain:{domain}\nreversed domain:{reverse}")
