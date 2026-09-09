"""wap to detect whether a comment is span or not.A comment should be treated as
spam or not.A comment should be treated as spam if it contains any of these keywords:
"make a lot of money","buy now","subscribe now","click this"."""
comment=input("Enter Comment:")
if comment=="make a lot of money"or comment=="buy now"or comment=="subscribe now"or comment=="click this":
    print("Spam detected!")
else:print("It is not a spam comment!")
