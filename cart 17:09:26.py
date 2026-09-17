#Write a menu driven python program where the user can add items,remove items,view cart,and exie
cart=[]
while True:
    print("1.Add Item\n")
    print("2.Remove Item\n")
    print("3.View Cart\n")
    print("4.Exit\n")
    choice=int(input("Enter your choice!"))
    if choice==1:
        item=input("Enter item to be added")
        cart.append(item)
        print("Item Added!")
    elif choice==2:
        item=input("Enter item to be removed")
        if item in cart:
         cart.remove(item)
        else:
           print("Invalid Item\n")
    elif choice==3:
       print("Cart:",cart)
    elif choice==4:
       print("Exiting...")
       break
    else:print("Invalid Choice")
    

