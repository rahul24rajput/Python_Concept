##########################################################################################################
################################################## CLASS #################################################
##########################################################################################################

# class :: A blue print / template/plan/models/design/

# object : A physial existence of a class
# An instance of a class

# class to object ---- >   one to many relation mean one class can have many object
# a physicial existence of a class called object or an instance of a class is nothing but a class.
# the variable that can used to refer a object called reference variable
# By using reference variable we can [perform required operations on the onject

##########################################################################################################
################################################## HOW TO DEFINE A  CLASS ################################
##########################################################################################################

# class Demo:
#     ''' this is a demo class '''
#     pass

# Now i want to access the doc string of this class
# so for this 
# print(Demo.__doc__) @ for getting the doc string information.

##########################################################################################################
################################################## TYPE OF VARIABLE INSIDE PYTHON CLASS ##################
##########################################################################################################
# there are three types of variable are allwoed in python class. 
# instance variable(object level variable)
# static variable(class level variable)
# local variable(method level cariables)

# Also there are three type of methods 
#  instance methods(object level variable)
# class methods(class level variable)
# static methods(method level cariables)


##########################################################################################################
################################################## Demo program to define and use a class ################
##########################################################################################################

# the function which are define inside the class are called method

# class student:
#     ''' class of student'''
#     def __init__(self, name, rollno, marks):              # special method
#         self.name = name
#         self.rollno = rollno
#         self.marks = marks

#     def talk(self):                      #### another method
#         print('helo i am', self.name)
#         print('my roll no', self.rollno)
#         print('my marks are', self.marks)
        
# # For creating an object 
# # reference variable = classname()
# s1 = student('sunny', 101, 90)
# s2 = student('bunny',102,95)


# class variable - -instance object, static class, local variable method

# class method  --  instance mehtod , static method, class method

############################################################################################
####################################3 self reference variable ##############################
############################################################################################

# self is a reference variable that is used for refereing current object
# within the class it is used to refer the current object

# class Test:
#     def __init__(self):
#         pass

# t = Test()
# now here you can not used this t (reference variable) within the class, bcz it is declare outside the class.
# so within the class you can use self reference variable to point to the object. and outside the class you can use 
# t reference variable to point to the object. 

# how can you say that self and t both are pointing to the same obj????

# so 
# class Test:
#     def __init__(self):
#         print(id(self))

# t = Test()
# print(id(t))

# O/P
# 140077047916304
# 140077047916304

################################################ EX-2 ###############################################33
# class Test:
#     def __init__(self):
#         print('constructor') # constructor method

#     def m1(self,x):  # general method
#         print('x value',x)class Test:
#     def __init__(self):
#         print(id(self))

# t = Test()
# print(id(t))


# t = Test() # contrucor will be called automatically
# t.m1(10)

################################################################################3
# To declare the instance variable we are using self
# self is used to declare the instance variable(means obkect level)

################################################3
# is self a keyword in python or not ????? 
#################################################

# class Sudent:
#     def __init__(delf,name ,rollno,marks):
#         delf.name= name
#         delf.rollno= rollno
#         delf.marks= marks
    
#     def talk(kelf):

#         print('name is',kelf.name) 
#         print('rollno is',kelf.rollno)
#         print('marks is',kelf.marks)
# s1 = Sudent("rahul", 1111, 4545) # so over here basically we are providing 3+1 = 4 value 3 explictly and one from PVM machine.
# s1.talk()

# self is not a keyword in python instead of self i can use any name.

# you can use anything in place of self beacuse self is not a keyword. so delf can be used to,
# but position should fixed. so this is more like argument passing.

# so basically here first argumentis always going to consider as implicit variable

#######################################################################################
######################### CONSTRUCTOR #################################################
#######################################################################################

# constructor is a special method in python. and in python the name of constructor is __init__ 
#  it will execute once per object .

# Purpose of constructor
#  just to declare and initlaized instance variable related to the object 

# class Sudent:
#     def __init__(delf,name ,rollno,marks):
#         delf.name= name               # instance variable
#         delf.rollno= rollno         # instance variable
#         delf.marks= marks          # instance variable
    
# s1 = Sudent("rahul", 1111, 4545) # so over here basically we are providing 3+1 = 4 value 3 explictly and one from PVM machine.
# print(s1.name,s1.rollno,s1.marks)

###########################################################################################
#################### CONSTRUCTOR PART 2 ###################################################
###########################################################################################

# This is a class without constructor method so is this a valid class or not ?
# class Test :
#     def demo(self):
#         print('method')

# t = Test()
# t.demo()

# A doubt can come here that if a class does not comtain constructor then how can you create a contructor?
#  _____________________________ans____________________________
# so within python class a constructor is always optional. if we are not writing any constructor then python will provide 
# default constructor

# EX______________________________________2

# class Test:
#     def __init__(self):
#         print("constructor executed")

# t = Test()
# t.__init__()
# t.__init__()
# t.__init__()

# ______________________________________________________________ OUTPUT_____________________________________
# constructor executed
# constructor executed
# constructor executed
# constructor executed
# ______________________________________________________________
# so four time constructor executed but only one object has created
# Is above the valid code or not ?
# whenever we are initalizing the object then we are not required to call constructor explictly
# but here we are calling constructr explictly so is it calid or not ?
# if is it valid then how many test object will be created

# ANS

# so if you can call init method explictly and and it will not create the new object . it will be executed 
# as a normal method  
# so in above code only one object will be created.

# _________________________________________EX-------3-_CONSTRUCTOR_____________________________
# class Test:
#     def __init__(self):
#         print('no arg constructor')

#     def __init__(self,x):
#         print('one arg constructor')
    
# t1 =  Test()  # Q here so in above class which constructor will be executed
# t2 = Test(10)# Q here so in above class which constructor will be executed

# So above class is invalid 
# in phython if there are two method with same name and different arg such type of method are called overloadaed methood.
# so in python method overloading concept is not there

# so in python,,,,, method overloading is not applicable

# so if you comment line no 218 then the last method will be execute  it will not execute first method.

################################################################################################################
#---------------------------------- PYTHON CLASS MINI APPLICATIOM ----------------------------------------------
################################################################################################################

# class Movie:
#     """ Thsi is a movie class"""
#     def __init__(self, title, hero,heroine):
#         self.title = title  # here self.title is called instance variable
#         self.hero = hero       # here self.hero is called instance variable
#         self.heroine = heroine  # here self.heroine is called instance variable
 
#     def info(self):
#         print('movie name', self.title)
#         print('hero name', self.hero)
#         print('heroine name', self.heroine)

# taking a list of movie object


# list_of_movies = []
# while True:
#     title = input('enter title name')
#     hero = input('enter hero name')
#     heroine = input('enter heroine name')
#     m = Movie(title,hero,heroine)
#     list_of_movies.append(m)
#     print('movie added successfully')
#     option = input('wanted to add one more movie -- yes/no')
#     if option.lower() == 'no':
#         break

# print("all movie information")

# for movie in list_of_movies:
#     movie.info()

# so here we have took the list for storing the data. so as long as program is executing then data will be stored in heap area
# but after execution finished then this data will be clear from heap memory. so for permanent storing the data we have to use either file or DB.


####################################################### one more example on constructor and class #######################33

# so in below calss basically we have not define the constructor and created a method same as the class name

# class Test:
    # def Test(self):
        # print('it is some special method')

# t = Test()  # it will not give any output
# t.Test()# it will give o/p as -- it is some special method
#------------------------------------------------------------------------
# Note ### -- is it possible to have class name as method name ???
# yes it is possible.
#--------------------------------------------------------------------------
# so from above line 277 it will call the default constructor as there is no constructor. and it will not execute the Test method
# we have to call this method explictly   

##########################################################################################################################
##################################### BASIC ABOUT TYPES OF VARIABLE ######################################################
##########################################################################################################################
# 1 instance variable [object level variable] -- if a value of a variable varied from object to object then such type of variable are called instance variable.
    # for every object  a seprate copy of instance variable will be created
#3 generllay inside constructor instance variable will be declared inside constructor by using self variable.
# class student:
#     def __init__(self, rollno,name):
#         self.rollno = rollno  # instance variable
#         self.name = name# instance variable
###################################################################################
# static variable [class level variable]
###################################################################################

# if a value of the variable not varied from object to object then it is never recommended to declare that variable as instance variable. declare it as a 
# static variable
# ex -- school name would not be change for every object so make it as a static variable


# class student:
    # school_name = "durgasoft" # static variable

    # def __init__(self, rollno, name):
        # self.rollno = rollno  # instance variable
        # self.name = name# # instance variable

# For instance variable a seprate copy will be created for every object. but for static variable class level variable only one copy will be created.
# that copy will be shared for every object


#################################################################################
# local variable [method level variable]
#################################################################################

# inside a method just to meet a temporary requirement sometimes we can declare variable are called local variable

# class student:
#     school_name = "durgasoft" # static variable

#     def __init__(self, rollno, name):
#         self.rollno = rollno  # instance variable
#         self.name = name# # instance variable
#     def info(self):
#         x = 10   # local variable
#         for i in range(x):
#             print(i)  
#         # so here i and x are local variable

# t = student(1010,"rahul")
# t.info()######### OUTPUT 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9


#################################################################
#  BASIC IDEA ABOUT TYPES OF METHOD-- INSTANCE,CLASS AND STATIC
#################################################################

# class stduent:
#     school_name = "durga"
    
#     def __init__(self, rollno, name):
#         self.rollno = rollno  # instance variable
#         self.name = name# # instance variable

#     def get_student_info(self): # instace method beacuse the first argument is self.
#         print('stident name', self.name)
#         print('stident name', self.rollno)

# inside a method  if we are trying to access at least one instance variable  then that method always talks about a particular
# object and that method should declared as instance method.
# STD ------  for the instance  method the first argumet always is self. so for any method if the first argument
#  is self then blindly iot is the instance method

    # def get_school_info(cls):
    #     print('school name', cls.school_name)
        # if i am using only static variable then the method is not related to particular object and it is related to class related method
        # that method have to declare as a class method.

## SYNTAX TO DECLARE A CLASS METHOD
# @classmethod
# def get_school_info(cls):
#     print('school name', cls.school_name)
# # what is cls here?????????????????????
# inside the method if we are using only static variables and if we are not using any instance variable then that method is no way related to 
# particular object and it is class level method. such type of method we have to declare as class level method.

# every thing in  python is object . even class is also a object.so for every class python one create one special object class level object
# so for student class one class level object will be created which will conatain class level info.

# cls is the reference variable. so for this class level object cls will be the reference variable c. cls will access the class level info
# 
# so if cls is there then this is class level object.  
#cls is the current class object reference variable. by using cls we can access class level data

## ----------------------------------------------------------------------------------------------------------------
# class Test:
#     @classmethod  # for declaring class level method
#     def m(cls):
#         print(id(cls))

# print(id(Test))
# t = Test()
# t.m()
## OUTPUT
# 140587392046488
# 140587392046488

############################################## STATIC METHOD ############################################
# IF  I AM NOT USING ANY INSTANCE VARIABLE AND STATIC VARIABLE # 
# JUST GENERAL UTILITY METHOD SO SUCH TYPE OF GENERAL UTILITY METHOD CALLED STATIC METHOD

# class Test:
#     @classmethod  # for declaring class level method
#     def m(cls):
#         print(id(cls))
    
#     def get_sum(a,b):
#         return a+b    # it will nowhere related to class and object 
#         # such type general uyility method declare as static method.

# # Declaring static method

# class stduent:
#     school_name = "durga"
    
#     def __init__(self, rollno, name):
#         self.rollno = rollno  # instance variable
#         self.name = name# # instance variable

#     def get_student_info(self): # instace method beacuse the first argument is self.
#         print('stident name', self.name)  # here i am using instance variable
#         print('stident name', self.rollno)

#     @classmethod
#     def get_school_info(cls):  # here i am using class level variable
#         print('school name', cls.school_name)

#     @staticmethod   # not using static and instance variable
#     def get_sum(a,b):
#         return a+b    # it will nowhere related to class and object 
        # such type general uyility method declare as static method.


##########################################################################################
#### Various places to declare instance variables
##########################################################################################

# inside constructor by using self
# inside instance method by using self
# outside of the class by using object reference variable

# class Test :
#     def __init__(self):
#         self.a = 10 # instance variable
#         self.b = 20 # instance variable


# t = Test()
# so here t contains teo reference variable
# print(t.__dict__) # so it is a object dictionary it will contain instance vaiable and value

########################## # inside instance method by using self######################################################
# class Test:
#     def __init__(self):
#         self.a = 10
#         self.b = 20
#     def m(self): # for instance method first argument is always is self
#         self.c = 30 # instance variable


# t = Test()

# print(t.__dict__) # here o/p -- {'a': 10, 'b': 20}::::---|||| c will not come, bcz it has been added inside m method
# so here when you create test object then init method automatically being called so in object a,b will be added
# but methos m is not being called so c is not added to the object
# t.m() #{'b': 20, 'a': 10, 'c': 30}  Now c will come
#-------------------------------------------------------------------------------------------------------------------------
########################## # outside of the class by using object reference variable######################################
#-------------------------------------------------------------------------------------------------------------------------
# in java this is not possible

# class Test:
#     def __init__(self):
#         self.a = 10
#         self.b = 20
#     def m(self): # for instance method first argument is always is self
#         self.c = 30 # instance variable


# t = Test()
# t.m() # print(t.__dict__) ---->{'b': 20, 'a': 10, 'c': 30}
# t.d = 40
# print(t.__dict__) #{'b': 20, 'd': 40, 'a': 10, 'c': 30}

#  if i create another object here then
# t2 = Test()
# print(t2.__dict__) # OUTPUT {'b': 20, 'a': 10,} so here c, d will not come as they not been added to this object

#########################################################################################################
######################### How to access Instance variables ##############################################
#########################################################################################################
# Inside a class you can access the instance vatibale using self and outside of the class it can be accessed using 
# reference variable

# class Test:
#     def __init__(self):
#         self.a = 10
#         self.b = 20
#     def display(self): # for instance method first argument is always is self
#         print(self.a)# accessing the instance variable inside the class
#         print(self.b)

# t = Test()
# t.display()

# print(t.a, t.b)# accessing the instance vatriable outside of the class

#########################################################################################################
######################### How to delete/update Instance variables ##############################################
#########################################################################################################
## not supported in java

# within the class then use 
# delf self.variable

# outside of the class
# def object reference.variable name

#del t.a


# class Test:
#     def __init__(self):
#         self.a = 10
#         self.b = 20
#         self.c = 20
#         self.d = 20
#         self.e = 20
#     def display(self): # for instance method first argument is always is self
#         del self.c
        

# t = Test()  # here a,b,c,d,e will be there all instance variable
# t.display() # but after calling this one c will be gone

# print(t.__dict__)# o/p {'e': 20, 'b': 20, 'd': 20, 'a': 10}

# t2 = Test()
# del t2.d,t2.e # deleting variable from outside of the variable
# print(t2.__dict__) ## o/p {'b': 20, 'c': 20, 'a': 10}

# The instance variable which are deleted from one object won't be deleted from other
# object, beacuse for every object separate copy will be there

## UPDATIG THE INSTACE VARIABLE

# t3 = Test()
# t3.a = 888
# t3.b = 999
# t4 = Test()
# print("t3", t3.a,t3.b)  # 888,999
# print("t2", t2.a,t2.b)  #  10,20


#########################################################################################
#### Various places to declare static variables
#########################################################################################
# if the value of a variable is not being changed object to object then we should go for static variable.

# class Student:
#     school_name = "durga_soft"   # static variable

#----------------------- Within the class directly but outside of any mehtod or constructor #----------- Define the static variable

# print(Student.__dict__)

#----------------------- Inside the constructor by using class name -----------------------------------------
# class Test:
#     a =10
#     def __init__(self):
         Test.b = 20  it will considered as static variable
# t = Test()

#----------------------- Inside the instance methos by using class name -----------------------------------------
# class Test:
#     a =10
#     def __init__(self):
#         Test.b = 20
#     def m(self):
#         Test.c = 50
# t = Test()
# t.m()

# print(Test.__dict__)
#OUTPUT----------------------------------------------------------------------
# {'m': <function Test.m at 0x7f3dc7ba6f28>, 'b': 20, '__module__': '__main__', '__doc__': None, 
# 'a': 10, '__weakref__': <attribute '__weakref__' of 'Test' objects>, 
# '__init__': <function Test.__init__ at 0x7f3dc7ba6d90>, 'c': 50, '__dict__': <attribute '__dict__' of 'Test' objects>}

#####
#----------------------- Inside the class method by using either cls or class name -----------------------------------------
# class Test:
#     a =10
#     def __init__(self):
#         Test.b = 20
#     def m(self):
#         Test.c = 50
#     @classmethod
#     def m2(cls):
#         cls.d = 60 # static variable can be access by using either cls or Class name
#         Test.e = 70
#     @staticmethod
#     def m3():
#         Test.f = 70
# t = Test()
# t.m2()
# ******************************************** VERY IMP POINT *********************************************
 Test.m2()  ----> m2 is a class method so it is not related to object have to access using class name
# Test.m3()


# Test.g = 70 #Outside of  the class by using class name 
# print(Test.__dict__)


##########################################################################################
#### How to access static variables
##########################################################################################
# we can access static variable either by object reference or class name


#inside constructor by using self or classsname
# class Test:
#     a = 10
#     def __init__(self):
#         print(self.a)
#         print(Test.a)

# t = Test()

#inside instance method by using self or classsname 
#inside  class method  by using  classsname
#inside  static method  by using  classsname
#outside of the class either by objec treference or by class name


# class Test:
#     a = 10
#     def __init__(self):
#         print(self.a)
#         print(Test.a)
#     def m(self):
#         print(self.a)
#         print(Test.a)
#     @classmethod
#     def cls_method(cls):
#         print(Test.a)
#     @staticmethod
#     def stc_method():
#         print(Test.a)


# t = Test()
# print(t.a)
# print(Test.a)#outside of the class either by objec treference or by class name
# Test.cls_method()
# Test.stc_method()


######################################################################
##### where wwe can modify the value of static variable
#######################################################################

# we can only modify the value of static variable using either class name or cls variable
# we can not modify static variable value using self or object reference

# class Test:
#     a =10
#     def __init__(self):
#         Test.a = 20  # by using thie test we can update static variable
#     # now taking instance method to see how can i update static variable
#     def instance_method(self):
#         Test.a = 30
#      # now taking class method to see how can i update static variable
#     @classmethod
#     def cls_meth(cls):
#         Test.a=40
#         cls.a = 50
#     # now taking static method to see how can i update static variable
#     @staticmethod
#     def stat_meth():
#         Test.a = 60

# t = Test()
# t.instance_method()
# Test.a = 1000
# Test.cls_meth()
# Test.stat_meth()
# print(Test.a)

##################################################################
Very Imp Below EX ### EX SET ON INSTANCE AND STATIC VARIABLE
##################################################################

# class Test:
#     x=10
#     def __init__(self):
#         self.y=20

# t1=Test()
# t2=Test()
# print('t1:',t1.x,t1.y) ## O/P: 10 20
# print('t2:',t2.x,t2.y) ## O/P:  10 20
# t1.x=888  # here we can not update the value of static variable by using reference variable. so here a new instance variable will be declared as a so by
# # using reference variable if we are trying to modify the value of static variable then the value will not be updated however a
# #  new instance variable will be created .
# t1.y=999
# print('t1:',t1.x,t1.y) ## O/P: 888, 999
# print('t2:',t2.x,t2.y) ## O/P: 10 20


# class Test:
#     x=10
#     def __init__(self):
#         self.y=20

# t1=Test()
# t2=Test()
# print('t1:',t1.x,t1.y) ## O/P: 10 20
# print('t2:',t2.x,t2.y) ## O/P:  10 20
# Test.x=888 
# Test.y=999
# print('t1:',t1.x,t1.y) ## O/P: 888, 20
# print('t2:',t2.x,t2.y) ## O/P: 888 20
# print('test',Test.a,Test.b) # o/p 888, 999

###############################################################################################
################ GETTER AND SETTER ############################################################
###############################################################################################
# IF YOU DONT KNOW THE value at the begning then you should go for getter and setter. but if you know the value at begning at the time of object creation 
# then constructor is good 
# class Std_data:
#     def setName(self,name):
#         self.name=name 

#     def getName(self):
#         return self.name
    
#     def setMarks(self,marks):
#         self.marks = marks
#     def getMarks(self):
#         return self.marks

# n = int(input("enter no of student"))
# student = []
# for i in range(n):
#     s = Std_data()
#     name = input("enter student name")
#     marks = int(input("enter marks"))
#     s.setName(name)
#     s.setMarks(marks)
#     student.append(s)

# for s in student:
#     print('hello',s.getName())
#     print('hello',s.getMarks())

###############################################################################################
#since static method is no where related to object . so it is highly recomnded not to create an object and call these method by the name of class name.
# class Durgasoft:
#     @staticmethod
#     def add(a,b):
#         return a+b

# for calling this static method no need to create a static method.
# Durgasoft.add(10,20)
# instance variable(at least one)+ static variable == Instance method
# instance variable(at least one)+ local variable ==  Instance method
# static variable + local variable === class methods
# local variable ===== static method

# for static methos @staticmethod decorator is optional. 
# so if a mehtod is not having any decorator then it can be instance method or static method
# instance mehtod can be called using obj and static methos can be called using class name.


######  inter q #########################  Question

# class Test:
#     def m():
#         print('some method')

# t = Test()
# t.m() # while calling this,,,, will give error as m one will be treated as instace method [bbcz i am not using any decorator. and calling this method 
#usings object reference so python will treat it as instance method so pvm will send a default  argument as self. so it will give error.

# class Test:
#     def m(x):
#         print('some method')

# t = Test()
# t.m() # this will work beacuse self arg will be passed and in m method i am using x as self.
# t.(10)# this will not work beacuse method is taking only one argument

# class Test:
#     def m(x):
#         print('some method')

# Test.m()# will be called as static method. BCZ we are calling using class name.

###############################################################################################################
############################################ INEER CLASS ######################################################
###############################################################################################################
# Sometimes we can declare a class inside another class,such type of classes are called inner classes.
# Without existing one type of object if there is no chance of existing another type of object,then we
# should go for inner classes.
# Example: Without existing Car object there is no chance of existing Engine object. Hence Engine
# class should be part of Car class.

# class Car:
#     .....
#     class Engien

# class Outer:
#     def __init__(self):
#         print("outer class object creation")

#     class Inner:
#         def __init__(self):
#             print("ineer class method")
#         def m1(self):
#             print("ineer class method")

# now i want to call m1 instance method. for that i need inner class object 

# outer_obj = Outer() # outer object created
# inner_obj = outer_obj.Inner() # creating inner object 
# inner_obj.m1()
######################################  second way of  ccreating inner class object and calling################
# i = Outer().Inner()
# i.m1()
##  OR ##
# i = Outer().Inner().m1()

#########################################  NESTED of ineer class ######################################################
# class Outer:
#     def __init__(self):
#         print("outer class object creation")

#     class Inner():
#         def __init__(self):
#             print("inner class 1 ")

#         class InnerInner():
#             def __init__(self):
#                 print("inner class level 2")
#             def m1(self):
#                 print("inner_inner class method called")

# way of calling m1 method

# outer_obj = Outer()
# inner_obj1 = outer_obj.Inner()
# inner_obj2 = inner_obj1.InnerInner()
# inner_obj2.m1()
### OR ####
# inner_obj2 = Outer().Inner().InnerInner().m1()

############################ CALLING A STATIC METHOD IN INNER CLASS ##################################################
# class Outer:
#     def __init__(self):
#         print("outer class object creation")

#     class Inner():
#         def __init__(self):
#             print("inner class 1 ")

#         class InnerInner():
#             def __init__(self):
#                 print("inner class level 2")
#             @staticmethod
#             def m1():
#                 print("inner_inner class method called")
    
# for calling a static method class object is not requiored {however we can call like this inner_obj2 = Outer().Inner().InnerInner().m1() }
# so here for m1 methos InnerInner class object is not required.
# Outer().Inner().InnerInner.m1()  ## look carefully i have not used InnerInner class object. i have called m1 using class name.

#######################################################################################################
########################## INNER CLASS DEMO ###########################################################
#######################################################################################################

# class Person:
#     def __init__(self,dd,mm,yy,name):
#         print("person object creation")
#         self.name = name
#         self.dob = self.Dob(dd,mm,yy)
#     def info(self):
#         print("name", self.name)
#         self.dob.display()

#     class Dob:
#         def __init__(self,dd,mm,yy):
#             print("dob obnject creation")
#             self.dd = dd
#             self.mm = mm
#             self.yy = yy
#         def display(self):
#             print("dob={}/{}/{}".format(self.dd,self.mm,self.yy))

# p = Person("durga",24,8,97)  #person object creation
# p.info()              #dob obnject creation
#               # Both object will be created here by default

#########################################################################################################
########################### NESTED METHOD ###############################################################
#########################################################################################################

# class Test:
#     def m1(self):
#         def calc(a,b):
#             a = 10
#             b = 20 
#             print("the su,",a+b)
#             print("the su,",a-b)
#             print("the su,",a*b)
#             print("the su,",a/b)
#         calc(10,20)

# t =Test()
# t.m1()

#####################################################################################
######################## GARBAGE COLLECTION AND DESTRUCTOR ##########################
#####################################################################################

# import gc
# print(gc.isenabled())
# i can disabled the gc 
# if there is no memory problems
# and there are very less number of object are created

# Destructor is a special method and the name should be __del__
# Just before destroying an object Garbage Collector always calls destructor to perform clean up
# activities (Resource deallocation activities like close database connection etc).
# Once destructor execution completed then Garbage Collector automatically destroys that object.
# Note: The job of destructor is not to destroy object and it is just to perform clean up activities.

# import time
# class Test:
#     def __init__(self):
#         print("Object Initialization...")
#     def __del__(self):
#         print("Fulfilling Last Wish and performing clean up activities...")
# t1=Test()
# t1=None # over here it has been dereferenced so it will automatically availble to garbage collector. so gc will
# # call destructor and then it will be deleted
# time.sleep(5)
# print("End of application") 

########################################### EXAMPLE 2 #########################
# import time
# class Test:
#     def __init__(self):
#         print("Object Initialization...")
#     def __del__(self):
#         print("Fulfilling Last Wish and performing clean up activities...")

# t1=Test()
# t2=Test()
# print("End of application") 
#after the 964 line __del__ will be called BY GC .
# the q is here will it call __del__ method or not. so gc will be called it doesn,t matter that they have dereferenced or not
# after the successfully execution of this class . heap memory has to be cleaned so these two object will not be used again and has to destroy 
# by gc  
 # at this point gc will destroy the both t1 and t2 obj. 

#-----------------------
#  OUTPUT
#-----------------------
# Object Initialization...
# Object Initialization...
# End of application
# Fulfilling Last Wish and performing clean up activities...
# Fulfilling Last Wish and performing clean up activities...
#--------------------------------------------------------------------

###################################################################################################
############## USING MEMBER OF ONE CLASS INSIDE ANOTHER CLASS #####################################
###################################################################################################
# TWO ways we can do it

# has a relationship -- composition 
# is-a relationship  -- inheritence

####################################################
############# HAS A RELATIONSHIP ###################
####################################################
# ex -- Class car has a engine relationship
# composite a bigger object with small small object called composition
# like with the help of tyre object, sheet object, engine object we can compose a car object 
# ex -----------------------------------------------------------
###########################################################################################
############################ HAS A RELATIONSHIP PROGRAM 1 #################################
###########################################################################################
# class Engine:
#     def __init__(self):
#         self.enginePower = "125KW"
#     def useEngine(self):
#         print("engine specific functionality")

# class Car:
#     def __init__(self):
#         self.engine = Engine() # creating a engine object

#     def useCar(self):
#         print('car required functionality')
#         self.engine.useEngine()
#         print(self.engine.enginePower)

# c = Car()
# c.useCar()
# above functionality called composition

###########################################################################################
############################ HAS A RELATIONSHIP PROGRAM 2 #################################
###########################################################################################

# class Car:
#     def __init__(self,name,model,color):
#         self.name = name 
#         self.model = model
#         self.color = color 

#     def getInfo(self):
#         print("car name: {}-{}-{}".format(self.name,self.color,self.model))

# # emp wants a car so creating a emp class

# class Emp:
#     def __init__(self,ename,eno,car):
#         self.ename = ename 
#         self.eno = eno 
#         self.car = car

#     def empInfo(self):
#         print("emp name",self.ename)
#         print("emp no",self.eno)
#         print("emp car info")
#         self.car.getInfo()

# c = Car("mahindra","V12","Red")
# e = Emp("rahul",4121,c)
# e.empInfo()


###########################################################################################
############################ HAS A RELATIONSHIP PROGRAM 3 #################################
###########################################################################################
# class SportsNews:
#     # def __init__(self):
#     #     print("this is sports news cjannel")
#     def sportsInfo(self):
#         print("kohali has been out today")

# class MovieNews:
#     # def __init__(self):
#     #     print("this is sMovieNewsports news cjannel")
#     def movieInfo(self):
#         print("tenent movie is coming")
# class PoliticsNews:
#     # def __init__(self):
#     #     print("this is PoliticsNews news cjannel")
#     def politicsInfo(self):
#         print(" ram is the new pm of india")


# class Durganews:
#     def __init__(self):
#         self.sports = SportsNews()
#         self.movie = MovieNews()
#         self.politics = PoliticsNews()

#     def getTotalNews(self):
#         print("Welcome to the news")
#         self.sports.sportsInfo()
#         self.movie.movieInfo()
#         self.politics.politicsInfo()


# c = Durganews()
# c.getTotalNews()

###########################################################################################
############################ HAS A RELATIONSHIP PROGRAM 4  ################################
###########################################################################################
# second apporach of doing same thing as done in above example
# news:
#     def __init__(self,sportsNews, movieNews, politicsNews):
#         self.sportsNews = sportsNews
#         self.movieNews = movieNews
#         self.politicsNews = politicsNews

#     def getTotalNews(self):
#         print("fdfd")

# sportsNews = SportsNews()
# movieNews = MovieNews()
# politicsNews = PoliticsNews()

# dnews = Durganews(sportsNews,movieNews,politicsNews)
# dnews.getTotalNews()
    
# class Durga

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ======================================= IS-A VS HAS- A Relationship ================================
#=====================================================================================================
# [if we want to extend existing functionality with some extra functionality then we should go for IS-A Relatuonship]
# [if we don't want to extend and just we have to use existing functionality then we should go for has a relationship]

# a emp can be a person # Is a relationship  Emp extending the person functionality
# a emp has a car       # Has a relationship Emp is just using car functionality but not responsible to extend car functionality

# class Car:
#     def __init__(self,name,color,model):
#         self.name = name
#         self.color= color
#         self.model = model
#     def get_info(self):
#         print("the car desc is {}{}{}".format(self.name,self.color,self.model))

# car = Car('inova','red','hunda')

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def entndrink(self):
#         print("eating biryania and drinking beer")

# p = Person('rahul',24)
# # IS A relationship Coinnection 
# class Emp(Person):   # inheriting a person class
#     def __init__(self,name,age,cmp_name,car):
#         super.__init__(name,age)
#         self.cmp_name= cmp_name
#         self.car = car
#     def getEmpDetail(self):
#         print('emp is a cse emp')

#     def empinfo(self):
#         print('emp name', self.name)
#         print('emp name', self.age)
#         print('emp name', self.cmp_name)
#         print('emp name', self.name)
#         print('emp name', self.name)
#         car.get_info()# emp using car functionaity

# e = Emp('dirga','24','qa',car)
# e.entndrink()
# e.empinfo()
#=======================================================================================================
#=================================== COMPOSITION VS AGGREGATION ========================================
#=======================================================================================================

# IF without existing the container object there is no chance of existing contained object then the container obj and contained object 
# are strongly associated. so this is called composition
# ex -- univeersity object is a container obj and department are the contained object
# without university object there will not be department object

########################################### Composition Example #####################################################

# class University:
#     def __init__(self, name,dept_name):
#         self.name=name
#         self.department=self.Department(dept_name)
#     def get_detail(self):
#         print('university name is',self.name)
#         self.department.dept_detail()
    
#     class Department:
#         def __init__(self,dept_name):
#             self.dept_name = dept_name
#         def dept_detail(self):
#             print('department name',self.dept_name)
# uny = University('RKGIT','CSE')
# uny.get_detail()
############################################ Aggreation Example #######################################################
# class University:
#     def __init__(self,name,dept):
#         self.name = name
#         self.dept = dept
#     def get_detail(self):
#         print('university naem is',self.name)
#         self.dept.dep_detail()
# class Department:
#     def __init__(self,dept_name):
#         self.dept_name = dept_name
#     def dep_detail(self):
#         print('separtment name',self.dept_name)

# dept = Department('CSE')
# uny = University('RKGIT',dept)
# uny.get_detail()

###############################################  TYPE OF INHERITENCE ###############################
# single Inheritence
# one parent class and one child class.
# the concept of inheriting from single parent class to single child class called single inheritence
# class Parent:
#     def parent_method(self):
#         print('parent class')

# class Child(Parent):
#     def child_method(self):
#         print('child method')
#     # for child class two method are presents
# c = Child() 
# c.parent_method()
# c.child_method()
# ##O/P
# parent class
# child method
#===========================================================================
# Multii level Inheritence
# The concept of inheriting members from multiple classes to a single class with the concept of one after another
# is known as a multilevel inheritence

# class GrandPArent:
#     def gp_method(self):
#         print('gp method')

# class Parent(GrandPArent):
#     def parent(self):
#         print('parent method')

# class Child(Parent):
#     def child(self):
#         print('child class')

# c = Child()
# c.gp_method()
# c.parent()
# c.child()
#============O/P
# gp method
# parent method
# child class
#########################################################################################################################
# Hierarchical Inheritence

                #      x
                #     / \
                #    /   \
                #    Y    Z
                #    /\
                #   /  \
                #  z    c      

            # parent is only one but many child
# The concept of inherting members from one class to multiple classes 
# which present at same level is known as Hierarchical inheritence

# class Parent:
#     def parent_method(self):
#         print('parent method')

# class childOne(Parent):
#     def childOneMethod(self):
#         print("child one obj")

# class childTwo(Parent):
#     def childTwoMethod(self):
#         print("child Two obj")
        
# c1 = childOne()
# c1.parent_method()
# c1.childOneMethod()
# c2 = childTwo()
# c2.parent_method()

#################################################################################
############## Multiple inheritence  Very Imp
#########################################################
# multiple means =------ multiple parents class and single child class is there

        #  p1               p2                    p3
        #  \                  |                   /
        #   \                 |                   /
        #                     Child Class

# class Parent1():
#     def m1(self):
#         print('parent one class')

# class Parent2():
#     def m2(self):
#         print('parent two class')
# class Child(Parent1,Parent2):   # Defining multiple inheritence
#     def m3(self):
#         print('child class')

# c = Child()
# c.m1()
# c.m2()
# c.m3()
############O/P
# parent one class
# parent two class
# child class

# Intervie q 
# Why java c sharp and other language won't support multiple inheritence?????
# So the q is here if parent1 is having m1 method and parent2 is having m1 method then in child class 
# which parent class method m1 will be executed ? [child.m1()]
# So this ambiguity problem occure and there is no way to solve this problm in java
# this is also called a dimoand problem
# So in multiple Inheritence the order of the class is very imp [class c (p1,p2)] order of p1 and p2
# so in python pvm will look for the m1 methos in child class if it is not found then it will look to p1 class.
# and execute the same.if the first parent does'nt contain the method then it will go to second parent .
# # 
# class P1():
#     def m1(self):
#         print('paraent one method')
# class P2():
#     def m1(self):
#         print('paraent seconf method')

# class Child(P1,P2):
#     def m2(self):
#         print('child mehthod')

# c = Child()
# c.m1()
## O/P
# paraent one method
# class Child(P2,P1):
#     def m2(self):
#         print('child mehthod')
# c = Child()
# c.m1()
##O/P
# paraent seconf method
#########################################################
# Hybris Inheritence # Combination of more than one type of inheritence called hybrid
# inheritence
#******************************************* MRO Read from PDF *******************************************

##################################################################
############################### SUPER FUNCTION ##################
#################################################################
# Super() is a built in function ehich is usefull to call the super class constructor, methods and variables explictly from the child class

# NEED of super function
# class P:
#     def m1(self):
#         print('parent method')

# class C(P):
#     def m2(self):
#         # i can call parent class m1 method like below
#         self.m1()
#         print('child method')

# c = C()
# c.m2()
# O/P#############3
# parent method
# child method

# ########### In above program child class was not having m1 method and this has to be called. so it was availble by parents
# to child  . so using self.m() it has worked.
# but now my problem is if child and parent class both are having same method m1 then how can i call parent class method explictly.
# bcz by using self.m1() it will call again child class m1() mehtod[it will refer the current child class method only]
# so m1 will internally call m1 there will be recursion

# How can i diffreniate between both method or how i can call explictly parent class method
#NAming conflict came so for that
# class P:
#     def m1(self):
#         print('parent method')

# class C(P):
#     def m2(self):
#         # i can call parent class m1 method like below
#         super().m1() # calling parent class method 
#         print('child method')

# c = C()
# c.m2()
# O/P#############3
# parent method
# child method
################################################3
# Demo program for super()

# class P:
#     a = 10
#     def __init__(self):
#         print('parent constructor')
#     def m1(self):
#         print('parent instance method')
#     @classmethod
#     def m2(cls):
#         print('parent class method')
#     @staticmethod
#     def m3():
#         print('parent static method')

# class C(P):
#     def __init__(self):
#         print('child constructor')
#     def method1(self):
#         print(super().a)
#         super().m1()# self.m1 will give the same result bcz there is no naming conflict in method
#         super().m2()#self.m2 will give the same result bcz there is no naming conflict in method
#         super().m3()#self.m3 will give the same result bcz there is no naming conflict in method
#         super().__init__()# Required super bcz there is naming conflit so for calling parent class init method need super

# c = C()
# c.method1()
######### O/P
# child constructor
# 10
# parent instance method
# parent instance method
# parent class method
# parent static method
# parent constructor
#############################################  SUPER EXAMPLE 2 ######################33
# class Person:
#     def __init__(self,name,age,height,weight):
#         self.name=name
#         self.age=age
#         self.height=height
#         self.weight=weight
#     def display(self):
#         print('name',self.name)
#         print('name',self.age)
#         print('name',self.height)
#         print('name',self.weight)

# class Student(Person):
#     def __init__(self,name, age,height,weight,rollno,marks):
        # self.name=name      # parent class already contain this variable but we did,nt use 
        # self.age=age        #parent class already contain this variable
        # self.height=height  #parent class already contain this variable
        # self.weight=weight  #parent class already contain this variable
        # self.rollno=rollno  
        # self.marks=marks
########So we cann call here parent class init method for above four variable.
#not require to write all above four lines, can be used from aprent class.
        # super().__init__(name,age,height,weight)
        # self.rollno=rollno
        # self.marks=marks

    # def display(self):
        # print('name',self.name)
        # print('name',self.age)
        # print('name',self.height)
        # print('name',self.weight)
        # above things can be called from parent class using super
        # print('name',self.rollno)
        # print('name',self.marks)
#         super().display()
#         print('name',self.rollno)
#         print('name',self.marks)

# s = Student('rahul',27,5,11.80,1358811,424)
# s.display()
##############O/P#######
# name rahul
# name 27
# name 5
# name 11.8
# name 1358811
# name 424

############################ SUPER CALLING EXAMPLE 3 ###################
# MULTILEVEL INHERITENCE
# class A:
#     def m1(self):
#         print('a class method')
# class B(A):
#     def m1(self):
#         print('b class method')
# class C(B):
#     def m1(self):
#         print('c class method')
# class D(C):
#     def m1(self):
#         print('d class method')
# class E(D):
#     def m1(self):
#         super().m1()#immediate parent method will get chance here so D class method will be called
#         #calling a particular class method using without super
#         B.m1(self) # now b class method will get the chance to be called.
#         # calling a particuar class method using super
#         super(C,self).m1() # but here c class method won't be called. here c class paraent B method will be called
#         print('e class method')

# e = E()
# e.m1() # e class method will be called 
##################################################
############ VERY IMP ############################
# in line 1490 so here the q is if i want to call either c class mehtod or b class method. to call a particular class method.
# how can i do ?
# so there are two ways of calling like this
# 1. way classname.methodname(self)
# in line 1490 can be done like  B.m(self)
# . way--- super(classname,self).m1() 
# so here whichever the classname is given the parent class method will be called of that classname.
##########################################################################################
# #######################  SUPER VS INSTANCE VARIABLES ###################################
# ########################################################################################

# loop hole in super. imp lec 313

# SUPER CAN NOT BE USED TO ACCESS PARENT CLASS INSTANCE VARIABLE.
# PARENT CLASS INSTANCE VARIABLE SHOULD BE ONLY ACCESS BY SELF 

# if parent and child class both are having same instance variable then you can not access
# parent class instance variable from child class . not even using super. 
#but we can use super to access parent class static variable

##########################################################################################33
#CAse 1
# class P:
#     a = 888
#     def __init__(self):
#         self.b=999

# class C(P):
#     def m1(self): # now inside m1 methos i want to access a,b variable written above Also [there is no naming 
#         #conflict between child and oarent variable so we can use dorectly self]
#          print(self.a)
#          print(self.b)
#          # here we use super also
#          print(super().a) # O/P-- 888
#          print(super().b) # it will give error [AttributeError: 'super' object has no attribute 'b']. super can't be used to acees parent class instance variable

# c = C()
# c.m1()
## O/P
# 888
# 999

### CAse 2 
# class P:
#     a = 888
#     def __init__(self):
#         self.b=999

# class C(P):
#     def __init__(self):
#         self.b = 20
#     def m1(self):
#         print(self.b)# it will always give the priority to child class instance variable
#         #but if you wanted to access here parent class instance variable then you can not. using super
#         # for accessing the parent class instance variable you haVE TO USE SELF. BUT FOR THAT child class4
#         # should not have the same variable

# c= C()
# c.m1()
################################################################# SUPER SPECIAL CASE 2######################33
#  class P:
#     a = 10
#     def __init__(self):
#         print('parent constructor')
#     def m1(self):
#         print('parent instance method')
#     @classmethod
#     def m2(cls):
#         print('parent class method')
#     @staticmethod
#     def m3():
#         print('parent static method')

# class C(P):
#     def __init__(self):
#         super().__init__() # you can call parent class init method from child class init method
#         super().m1() # you can call parent class m1 method from child class init method
#         super().m2() # you can call parent class m2 method from child class init method
#         super().m3() # you can call parent class m3 method from child class init method
#     def method1(self):
#         super().__init__() # you can call parent class init method from child class method1
#         super().m1()  #you can call parent class m1 method from child class method1
#         super().m2()  #you can call parent class m1 method from child class  method1
#         super().m3()  #you can call parent class m1 method from child class  method1
#     @classmethod
#     def method2(cls):
#         super().__init__() # ypou can't call parent class init method from child class classm method [bcz class method no way related to object but constructor and init method require object] 
#         super().m1()   # ypou can't call parent class init method from child class classm method
#         super().m2()   # Can be called
#         super().m3()   # can be called 
#     @staticmethod
#     def method3():
#         super().__init__() # can not be called 
#         super().m1()       # can not be called
#         super().m2()     # can not be called
#         super().m3()     # can not be called
        
 # child class method2 can be called simply like below
#  C.method2() # no object required
#c = C()

#########################3
#from class method of child class how to call parent class constructor and instance method

# class P():
#     def __init__(self):
#         print('parent constructor')

#     def m1(self):
#         print('parent instance method')


# class C(P):
#     @classmethod
#     def m2(cls):
#         super(C,cls).__init__(cls)## calling parent classs init method
#         super(C,cls).m1(cls)# calling parent class m1 method
    
# c = C()
# c.m2()
########### O/P
# parent constructor
# parent constructor
# parent instance method

####3*************************************************************************************
#from static method of child class how to call parent class static and class method
# class P():
#     @classmethod
#     def m2(cls):
#         print('parent class method')

#     @staticmethod
#     def m3():
#         print('parent static method')

# class C(P):
#     @staticmethod
#     def m2():
#         super(C,C).m2()
#         super(C,C).m3()
# C.m2()
## O/P
# parent class method
# parent static method
######################################################################################################3
################################## POLYMORPHISM #######################################################3
##########################################################################################################

# Enhancement of durga pdf example given 
# Please study the rest of content from durga pdf page no 262

# class Book:
#     def __init__(self,pages):
#         self.pages=pages
#     def __add__(self,other):
#         return self.pages+other.pages
# b1=Book(100)
# b2=Book(200)
# b3 = Book(300)
# print(b1+b2+b3)   # TypeError: unsupported operand type(s) for +: 'int' and 'Book'
# bcz here b1+b2 wil give int value and it can not be add book type of object
####################################################################################
#  How can i add more than three object
# class Book:
#     def __init__(self,pages):
#         self.pages = pages
        
    
# b1 = Book(100)
# b2 = Book(200)
# b3 = Book(300)

# print(b1+b2) # TypeError: unsupported operand type(s) for +: 'Book' and 'Book'                                                                               

# Now i am gona implemented magic method __add__
# class Book:
#     def __init__(self,pages):
#         self.pages = pages
#     def __add__(self,other):
#         return Book(self.pages+other.pages) # making a book object
#     def __str__(self):
#         return 'the total pages {}'.format(self.pages)
# b1 = Book(100)
# b2 = Book(200)
# b3 = Book(300)

# print(b1+b2) # O/P --> 300
# print(b1+b2+b3)# TypeError: unsupported operand type(s) for +: 'int' and 'Book'                                                                                
# so for avoiding the above error i need to return book type of object instead of int obj
# so for that Book(self.pages+other.pages) will come
################ O/P ######################
# <__main__.Book object at 0x7ffaf43c47b8>                                                                                                      
# <__main__.Book object at 0x7ffaf43c4828>  Getting object format now need in understandable string format

# so for that implement __Str__ method
#############################################################################################################
########################### __STR__ METHOD ##################################################################
#############################################################################################################

# whenever we are trying to print any objectreference internally __str__() meathod will be called
# the default implementation of this method returns the string in th following format
# <__main__.Student object at 0x7f3f8ab7a128>  
# To provide meaningfull string representation for ouR object we have to override __str__() methos in  our class
# class Student:
#     def __init__(self,name,rollno,marks):
#         self.name = name
#         self.rollno = rollno
#         self.marks = marks
        
# s1 = Student('durga',101,95)
# s2 = Student('rahul',151,98)
# when we try to print any object reference [s1] then it will internally call __str__ method will be called
# it will provide the default implementation as  string format. 
#print(s1)  # O/P <__main__.Student object at 0x7f3f8ab7a128>                                                                                                   
# now if you want to provide meaningfull string implementation then you should implement __str__ method

# So we have to override __Str__ mrthod
############################
# class Student:
#     def __init__(self,name,rollno,marks):
#         self.name = name
#         self.rollno = rollno
#         self.marks = marks
#     def __str__(self):
#         # return self.name
#         #or
#         return 'name: {}, rollno {}, marks {}'.format(self.name,self.rollno,self.marks)
        
# s1 = Student('durga',101,95)
# s2 = Student('rahul',151,98)
# so now when i try to print any object reference i can get name and all remaining things along with it
# print(s1)
# O/P
# durga
    #or
# name: durga, rollno 101, marks 95                                                                                                             



#####################################################################################
################ METHOD OVERLOADING #################################################
#####################################################################################
BAsic structure of methos overloading
public class Sum { 
  
    // Overloaded sum(). This sum takes two int parameters 
    public int sum(int x, int y) 
    { 
        return (x + y); 
    } 
  
    // Overloaded sum(). This sum takes three int parameters 
    public int sum(int x, int y, int z) 
    { 
        return (x + y + z); 
    } 
##################################################################


# Rest of theory read from pdf
# Why python does not provide method OVERLOADING  ???????????????
# Two method are said to be overloaded iff both methods having same name but different arguments types
# eg :
#     sqrt(int)
#     sqrt(float)
# but in python we can not declare type of argument explictly.Based on python value type will be considered 
# automatically (Dynamic typed). As type concepr is not applicable method overloading concept is not applicable in python

# Way of knowing or getting method overloading
# class Test:
    # def method1(self,x):
        # print('{}-argument-method'.format(x.__class__.__name__))

## STD ##
# if you know the name of the variable so how to print corresponding type
# type(x) #O/p <class, int> but here i dont want class 
# so i want only int for that??
#x.__class__ # it will give the corresponding class ===>>>> <class 'int'>-argument-method                                                                                                                 
#x.__class__.__name__ # it will the corresponding class name like int ==>>> int

# t = Test()
# t.method1(10) # int-argument-method                                                                                                                           
# t.method1(10.5) #    float-argument-method
# So in python we dont need same method with different different argument. in python we can do with one method.  
