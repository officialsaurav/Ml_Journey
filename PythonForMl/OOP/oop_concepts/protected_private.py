class A:
    def __init__(self):
        self._protected_var = "I am a protected variable"
        self.__private_var = "I am a private variable"

    def get_private_var(self):
        print(self.__private_var)


a=A()
print(a._protected_var)
a.get_private_var()
# a.__private_var