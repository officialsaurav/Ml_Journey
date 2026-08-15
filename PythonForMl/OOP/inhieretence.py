#single
class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def start_engine(self):
        return f" the {self.brand} vehicle of {self.model} model's engine started."

class Car(Vehicle):
    def __init__(self,brand,model,number_of_doors):
        super().__init__(brand,model)
        self.number_of_doors=number_of_doors
    def drive(self):
        return f"The {self.model} is driving with {self.number_of_doors} doors."

family_car=Car("honda","civic",4)
print(family_car.drive(),family_car.start_engine())

#simple eg

class Vehic:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

class Carr(Vehic):
    def engine(self):
        print(f"The engine of {self.brand} {self.model} is started.")

c=Carr("hondai","Venue")
c.engine()

# multylevel inheritance
class Grandparent:
    def wishdom(self):
        return "experience matters"
class Parent(Grandparent):
    def advice(self):
        return "plan for the future"

class Child(Parent):
    def fun(self):
        return "Live in the moment"


c=Child()

print(c.fun(),
c.advice(),
c.wishdom())

#hierarchial inheritance

class V:
    def start(self):
        return "Starting..."

class C(V):
    def type(self,model):
        self.model=model
        return f"The type of car is {self.model}"

class bike(V):
    def info(self):
        return "its a bike"


b=bike()
print(b.start(),b.info() )
c=C()
print(c.start(),c.type("sedan"))