#eg of polymorphysm: The make_sound() function accepts any object that has a sound() method, demonstrating polymorphism in
#action.


class Bird:
    def sound(self):
        return "Chirp"

class Dog:
    def sound (self):
        return "Bark"


def make_sound(animal):
    print(animal.sound())


dog=Dog()
make_sound(Bird())
make_sound(dog)



#compile time
class Calculator:
    def multiply(self, a=1, b=1, *args):
        result = a * b
        for num in args:
           result *= num
        return result

calc = Calculator()
# Using default arguments
print(calc.multiply())
print(calc.multiply(4))
# Using multiple arguments
print(calc.multiply(2, 3))
print(calc.multiply(2, 3, 4))
#output ⇒ 1,4,6,24






#compile time polymorphysm

class Animal:
    def sound(self):
        return "Some generic sound"
class Dog(Animal):
    def sound(self):
        return "Bark"
class Cat(Animal):
    def sound(self):
        return "Meow"
# Polymorphic behavior
animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.sound())



#duck typing polymorphysm

class Student:
    def study(self):
        print("Student is studying.")

class Teacher:
    def study(self):
        print("Teacher is preparing lessons.")

# Duck Typing function out of class

def do_study(person):
        person.study()  #takes class object as parameter and calls the method study() of that class object

do_study(Student()) # Student is studying.
do_study(Teacher()) # Teacher is preparing lesson