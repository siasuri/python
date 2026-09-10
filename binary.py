#wap to input a decimal number and convert it into binary without using the built-in bin() function
no=int(input("Enter a decimal number:"))
binary = ""

while no > 0:
    rem = no % 2
    binary = str(rem) + binary
    no = no // 2

print("Binary number:", binary)
