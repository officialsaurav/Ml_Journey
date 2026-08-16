class Employee:
    def __init__(self,salary):
        self.__salary = 50000  # Private attribute
    @property
    def salary(self):
        return self.__salary  
    @salary.setter
    def salary(self, amount):
        self.__salary = amount  
        
emp=Employee(5000)
print(emp.salary)
emp.salary=6000
print(emp.salary)  
