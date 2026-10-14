""" Create a object and object: Student details
Problem:Create a Student class to store a Student's name and roll no.Create an object and 
display the details using an instance method."""
class Student:
    def set_details(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)


s1 = Student()

s1.set_details("Sia", 17)

s1.display()
