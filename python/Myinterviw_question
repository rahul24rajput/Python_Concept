Accessing __init__ vars in classmethod 

class Test:
    def __init__(self):
        self.a = 10
    
    @classmethod    
    def cls_method(cls):
        self=cls()
        print(self.a)
        
t = Test()
t.cls_method()
