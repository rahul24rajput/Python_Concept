from django.contrib import admin
from news.models import StudentsTable
# Register your models here.


#### 2nd these line were added
# Now from here i am adding a class to see all the data in admin interface. Currently defined __str__ method in news.model.py
# will give you only name . so you can see only name in admin interface. Now if you want to see all colums information
#  then you have to define a class here in admin.py 
class StudentsTableAdmin(admin.ModelAdmin):
    list_display = ['name','marks']



# 1  st these line were added
# If you wanted to see your data as name in admin then register your data here
# admin.site.register(StudentsTableAdmin,TeacherTableAdmin) # have to register the StudentsTable here to see in admin interface
admin.site.register(StudentsTable,StudentsTableAdmin)