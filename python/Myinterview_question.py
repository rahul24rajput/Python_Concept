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
