""" Create a product class with the product name,price and quantity.Add an instance method to calculate
the total cost.Take these values from the user and display the product name and total cost
"""
class product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def total(self):
        return self.price*self.quantity
name=input("Enter product name:")
price=int(input("Enter product price:"))
quantity=int(input("Enter product quantity:"))
product1=product(name,price,quantity)
print("Product:",product1.name)
print("Total:",product1.total())
