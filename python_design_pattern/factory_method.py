# A factory method is a short of method which initialize the object.
# A Factory is an object for creating other objects.
# So a factory method is an alternative to initialize.
#### Example 1 

from enum import Enum
from math import *

class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2
    
class Point:
    def __init__(self,a,b,system=CoordinateSystem.CARTESIAN):
        if system = CoordinateSystem.CARTESIAN:
            self.x =a
            self.y =b
        elif system = CoordinateSystem.POLAR:
            self.x = a * cos(b)
            self.y = a * sin(b) 
        
    # ^^^^^^^^^^^^^^^^^^^^  Before Factory Mehtod
        
#So we have a scenario which is particularly painful it's particularly painful because imagine you introduce
# another coordinate system what you would have to do is you would have to change the enum here so you
# would have to have another member of the unit.
# But in addition you would also have to have another check ( if-else) inside the constructor kind of breaks the
# open closed principle in a way and in any case what's happening.
# It's not so much the open closed principle does the problem is the fact that these things are called
# a and b that you have to somehow figure out that a maps to X and B maps to Y when you're doing Cartesian
# for example so it's all very inconvenient which is why instead of using the initialize that we do something
# different.  And create the factory method

  #   After Factory Mehtod  

    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return('{}{}'.format(self.x,self.y))
    
    @staticmethod                 # this is also a way to instantaing the class or                             
    def new_cartesian_point(x,y): #creating a class object.using static method
        return Point(x,y)
    
    @staticmethod
    def new_polar_point(roh,theta):
         return Point(roh*sin(theta),roh*cos(theta ))
pb1 = Point.new_cartesian_point(2,3)          
pb2 = Point.new_polar_point(2,3)
print(pb1,pb2,sep='\n')

         
    # After factory mrthod and Grouping into seprate class
class PointFactory:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return('{}{}'.format(self.x,self.y))
    
    @staticmethod                 # this is also a way to instantaing the class or                             
    def new_cartesian_point(x,y): #creating a class object.using static method
        return Point(x,y)
    
    @staticmethod
    def new_polar_point(roh,theta):
         return Point(roh*sin(theta),roh*cos(theta ))
         
pb1 = PointFactory.new_cartesian_point(2,3)          
pb2 = PointFactory.new_polar_point(2,3)
print(pb1,pb2,sep='\n')

##################################    Example 2   #######################################
class EnglishTranslator:
    def __init__(self):
        print('This is Eng ttranslator')
        
    def method1(self):
        pass
    
class GreekTranslator:
    def __init__(self):
        print('This is greek translator')
        
    def method(self):
        pass
    
    
def factory_method(language):
    translator= {
        'English': EnglishTranslator,
        'Greek' : GreekTranslator
    }
    return translator[language]()
    
factory_method('English')
factory_method('Greek')
    
    
    
        


