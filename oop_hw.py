#Q1 Create a Class Line which has methods to accept coordindates as set of Tuples, a method that calculates the slope of line and distance of life
import math 

class Line:

    def __init__(self,coor1 = (0,0) , coor2 = (0,0)):
        self.x1, self.y1 = coor1
        self.x2, self.y2 = coor2

    def distance(self):
       return math.sqrt( (self.x2-self.x1)**2 + (self.y2-self.y1) **2 )
    
    def slope(self):
        if (self.x2 - self.x1) != 0:
            return ( (self.y2 - self.y1) / (self.x2 - self.x1))
        else:
            return 'infinity'


# line1 = Line((2,2) , (2,4))
# print(line1.distance())
# print(line1.slope())


# Q2 Create a cylinder class which accepts height and radius and create methods to return Volume and surface_area respectively

class Cylinder:

    def __init__(self, height = 1, radius = 1):
        self.height = height
        self.radius = radius

    def Volume(self):
        return math.pi * self.radius**2 * self.height
    
    def surface_area(self):
        return 2 * (math.pi*self.radius*self.height + math.pi*self.radius**2)
    
cyl = Cylinder(64, 5)
print(cyl.Volume())
print(cyl.surface_area())