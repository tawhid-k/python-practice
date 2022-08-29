import math

class Cylinder:
    radius = 5
    height = 15
    def __init__(self, radius, height):
        print('Default radius='+str(Cylinder.radius)+' and height='+str(Cylinder.height))
        Cylinder.height = height
        Cylinder.radius = radius
        print('Updated radius='+str(Cylinder.radius)+' and height='+str(Cylinder.height))
    
    @staticmethod  
    def area(radius, height):
        area = ((2*math.pi*radius*radius) + (2*math.pi*radius*height))
        print('Area: ' + str(area))
    
    @staticmethod 
    def volume(radius, height):
        volume = (math.pi*radius*radius*height)
        print('Volume: ' + str(volume))
    
    @staticmethod 
    def swap(height, radius):
        return Cylinder(radius, height)
    
    @staticmethod 
    def changeFormat(st):
        radius, height = map(int, st.split('-'))
        return Cylinder(radius, height)
    
c1 = Cylinder(0,0)
Cylinder.area(c1.radius,c1.height)
Cylinder.volume(c1.radius,c1.height)
print("===============================")
c2 = Cylinder.swap(8,3)
c2.area(c2.radius,c2.height)
c2.volume(c2.radius,c2.height)
print("===============================")
c3 = Cylinder.changeFormat("7-13")
c3.area(c3.radius,c3.height)
c3.volume(c3.radius,c3.height)
print("===============================")
Cylinder(0.3,5.56).area(Cylinder.radius,Cylinder.height)
print("===============================")
Cylinder(3,5).volume(Cylinder.radius,Cylinder.height)
