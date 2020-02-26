# # Liskov subsitute principle
# The principle was introduced by Barbara Liskov in 1987 and according to this principle “Derived or 
# child classes must be substitutable for their base or parent classes“. This principle ensures that 
# any class that is the child of a parent class should be usable in place of its parent without any 
# unexpected behavior.
# You can understand it in a way that a farmer’s son should inherit farming skills from his father
# and should be able to replace his father if needed. If the son wants to become a farmer then he can 
# replace his father but if he wants to become a cricketer then definitely the son can’t replace his father 
# even though they both belong to the same family hierarchy.

class Rectangle:
    def __init__(self,height,width):
        self._height = height
        self._width = width
    @property
    def height(self):
        return self._height
    @property
    def width(self):
        return self._width 
    @property
    def area(self):
        return self._height * self._width
        
    @height.setter
    def height(self,height):
        self._height = height
        
    @width.setter
    def width(self,width):
        self._width = width
    def __str__(self):
        return ('{}{}'.format(self.height,self.width))


# defining a class square that inherits from rectangle. bcz every square is a rectangle         
class Square(Rectangle):
    def __init__(self,size): # size is width and height
        super().__init__(size,size)
    # as a square property that width and height are equal
    # so define that property
    
    
    @property
    def width(self):
        return self._width
        
    @width.setter
    def width(self,value):
         self._width =self._height = value
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self,value):
         self._width =self._height = value

    @width.setter
    def width(self,value):
        self._width =self._height = value

        
def use_it(rc):
    w = rc.width
    rc.height = 10
    expected =  w * 10
    print('expected {},, and got this {}'.format(expected, rc.area))
    
r = Rectangle(10,20)
use_it(r)
    
sq = Square(5)
use_it(sq)
