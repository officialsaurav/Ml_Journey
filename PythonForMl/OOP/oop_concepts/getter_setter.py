class Employee:
    def __init__(self):
        self.__salary = 50000  # Private attribute

    def get_salary(self):
        return self.__salary  
    def set_salary(self, amount):
        self.__salary += amount  
        
emp1=Employee()
print(emp1.get_salary())  
emp1.set_salary(11)
print(emp1.get_salary())
