# Advanced model concepts
# Model Inheritence
# it has basically four types:

# Abstract Base Class Model Inheritance
# Multi table Inheritance
# Proxy Model Inheritance
# Multiple Inheritance

#====================================================================================
# Abstract Base Class Model Inheritance
#====================================================================================
let say thete are two models and they are having same field then it is highly recomanded not to use create
these fields in both model. So hare what can we do we can create a Basemodel and inherit the data fields from 
BaseModel and use it in both models. So below in both model here there are some fields are common
so for these fields we can create a seprate base model 

from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=64)
    email=models.EmailField()
    address=models.CharField(max_length=256)
    rollno=models.IntegerField()
    marks=models.IntegerField()

class Teacher(models.Model):
    name=models.CharField(max_length=64)
    email=models.EmailField()
    address=models.CharField(max_length=256)
    subject=models.CharField(max_length=64)
    salary=models.FloatField()

###################  CREATING A BASE MDOEL HERE #######################

# CotnactInfo class is an abstract class and hence table won't be created.
#   It is not possible to register abstract model classes to the admin interface.If we are trying
#  to do then we will get error.

class ContactInfo(models.Model):
    name=models.CharField(max_length=64)
    email=models.EmailField()
    address=models.CharField(max_length=256)
    class Meta:
        abstract=True

# Now here i can inherit these two models in Student and teacher
class Student(ContactInfo):
    rollno=models.IntegerField()
    marks=models.IntegerField()

class Teacher(ContactInfo):
    subject=models.CharField(max_length=64)
    salary=models.FloatField()

# So this is how Abstract base class model works.

#====================================================================================
# Multi Table Inheritance
#====================================================================================
# if the base class is not abstract then it will be multi table inheritence,So over here for the base 
# model table will be created Internally .

# In Multitable inheritance, inside database tables will be created for both Parent and
# Child classes. Multi table inheritance uses an implicit OneToOneField to link Parent
# and Child. i.e by using one-to-one relationship multi table inheritance is internally
# implemented.
# Django hides internal structure and creates feeling that both tables are independent. 

class BaseModel(models.Model):
    f1=models.CharField(max_length=64)
    f2=models.CharField(max_length=64)
    f3=models.CharField(max_length=64)

This is how the table will  be created
# field
# id   
# f1
# f2
# f3
class StandardModel(BaseModel):
    f4=models.CharField(max_length=64)
    f5=models.CharField(max_length=64)
#Filed 
#basemodel_id  =====> #will be used here as foreign key
#f4
#f5

#====================================================================================
# Multi Level Inheritance:
#====================================================================================

class Person(models.Model):
    name=models.CharField(max_length=64)
    age=models.IntegerField()

class Employee(Person):
    eno=models.IntegerField()
    esal=models.FloatField()

class Manager(Employee):
    exp=models.IntegerField()
    team_size=models.IntegerField()


#====================================================================================
# Multiple Inheritance:
#====================================================================================
class Person(models.Model):
    f1 = models.charField(max_length=64)
    f2 = models.charField(max_length=64)

class Person2(models.Model):
    f3 = models.charField(max_length=64)
    f4 = models.charField(max_length=64)

class Person3(Person,Person2):
    f5 = models.charField(max_length=64)
    f6 = models.charField(max_length=64)

# Multiple inheritence is treated as nulti table inheritence only
# Also we should not have any common field in the parent classes 
# otherwise we will get error]

#======================================================
# Model Manager
#======================================================
# Model manager is used to intrect with the database,Manager is some kind of 'gate' between application and database.
#  By default model manager is availble through 
# model.objects.property, i.e modelproperty type 
# Purpose of model manager is interacting with database. To get default model manager we can use
# Model.onjects property
# model manager is of what type?
# it is django.db.models.manager.Manager

# >>> from testapp.models import Employee
#  >>> type(Employee.objects)
#  <class 'django.db.models.manager.Manager'>

##########################################
## Defining our own custom model manager
##########################################
# If we want to define our own custom model manager then we have to write chils class of 
# models.Manager
Whenever we are using all() method, internally it will call get_queryset() method. To customize this behaviour
we have to override get_queryset method 

class customManager(models.Manager):
    def get_queryset(self):
        super().get_queryset().order_by('eno')

class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=64)
    esal=models.FloatField()
    eaddr=models.CharField(max_length=256)
    objects=CustomManager() ## here we have used the custom manager to executing the query

# When ever we are using all() method it will always get employees in ascending order of
# eno

# based on our requirement we can define more methods in customManager
# so that can be used in view.py please check the below customManager class and view.py file
class CustomModelManager(models.Manager):
    def get_queryset(self):
        super().get_queryset().order_by('eno')

    def  get_emp_salry_range(self,esal1,esal2):
        super().get_queryset().filter(esal__range=(esal1,esal2))

    def get_employee_stored_by(self,param):
        super().get_queryset().order_by(param)

# Now in view.py this is what we can do for better understanding
def display_view(request):
    employess = Employee.objects.get_employee_stored_by('esal'):
    ##
    ##
    ##==>> Notice here that we are using custom method has been defined in custom manager



#======================================================
# PROXY MODEL 
#======================================================

# IN THE MULti table inheritance ALWAYS a new table is created but in the Proxy
# new table would not be created , 
# THE MULti table inheritance new database table is created for each subclass of a model. This is usually the desired behavior, 
# since the subclass needs a place to store any additional data fields that are not present on the 
# base class. Sometimes, however, you only want to change the Python behavior of a model – perhaps
# to change the default manager, or add a new method.

# -------------------------------
# Inside models.py
# -------------------------------
class CustomModelManager1(models.Manager):
    def get_queryset(self):
        super().get_queryset().order_by('eno')

class CustomManager2(models.Manager):
    def  get_emp_salry_range(self,esal1,esal2):
        super().get_queryset().filter(esal__range=(esal1,esal2))

class CustomManager3(models.Manager):
    def get_employee_stored_by(self,param):
        super().get_queryset().order_by(param)

class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=64)
    esal=models.FloatField()
    eaddr=models.CharField(max_length=256)
    objects=CustomManager() 

class ProxyEmpolyee(Employee):
    objects = CustomManager2()
    class Meta:
        proxy = True

class ProxyEmpolyee2(Employee):
    objects= CustomManager3()

    class Meta:
        proxy = True

#  Both Employee and ProxyEmployee are pointing to the same table only.

# in view.py we can do this
fromdjango.shortcutsimportrender
fromtestapp.modelsimportEmployee,ProxyEmployee,ProxyEmployee2
 #Createyourviewshere.
def display_view(request):
    # employees=Employee.objects.all()
    # employees=ProxyEmployee.objects.all()
    employees=ProxyEmployee2.objects.all()
    my_dict={'employees':employees}
    return render(request,'testapp/index.html',my_dict)

# So we can use one model in different diferent view , without even altering it
Very Imp below rule
For the same Model we can provide a customized view without touching the database
is possible by using Proxy Model Inheritance.