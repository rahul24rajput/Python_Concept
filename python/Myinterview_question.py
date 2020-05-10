# Accessing __init__ vars in classmetho
# this shows the way that how can we access the init variables inside class method, wherever class method is no way related 
# to object

class Test:
    def __init__(self):
        self.a = 10
    
    @classmethod    
    def cls_method(cls):
        self=cls()
        print(self.a)
        
t = Test()
t.cls_method()
#############

#To get the file name
print(__file__)
# To know the absolute path of current file python file
print(os.path.abspath(__file__))
# /Users/kbhatnagar/Desktop/temp/temp.py. 
# To know the base directory name of current file
print(os.path.dirname(os.path.abspath(__file__)))
# /Users/kbhatnagar/Desktop/temp will come
