class P():
    def greet(self):
        print("Hello from parent")
class C(P):
    def greet(self):
        print("Hello from child")

c=C()
c.greet()
P().greet()


# eg to override __str__ method
class Author:
    def book(self, date, title):
        self.date=date
        self.title=title
        return f"{self.title} and  {self.date}"
    def __str__(self):
        return f"{self.title} was published in {self.date}"

a=Author()
a.book(2020,"Python")
print(a) #this calls the __str__ method of the class and prints the string returned by it print(a.__str__()) #same as print(a)
print(a.__str__()) #same as print(a)
print(a.book(100,"haha")) #none is printed because book method does not return anything
print(a) #this will print the same as before because __str__ method is called when we print the object


#-----------------------------
class a:
    def __init__(self):
        print("parent class constructor")

class b(a):
    pass
c=b()