#__mul__

class Vector2d:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __mul__(self,other):
        if isinstance(other,(int,float)):
            return Vector2d(self.x*other,self.y*other)
        return  Vector2d(self.x*other.x,self.y*other.y)

v1=Vector2d(2,3)
v2=Vector2d(4,5)
v3=v1*v2
v4=v1*2
v5=v3*3
print(v3.x,v3.y)
print(v4.x,v4.y)
print(v5.x,v5.y)
print(v2*1) ##

#=================================================================================================
#truediv

class Vector2d:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __truediv__(self,other):
        if isinstance(other,(int,float)):
            return Vector2d(self.x/other,self.y/other)
        return  Vector2d(self.x/other.x,self.y/other.y)

v1=Vector2d(4,8)
v2=Vector2d(2,4)
v3=v1/v2
v4=v1/2
print(v3.x,v3.y)
print(v4.x,v4.y)