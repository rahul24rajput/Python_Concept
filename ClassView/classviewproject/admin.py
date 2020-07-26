from django.contrib import admin
from classviewproject.models import Book , ContactInfoSecond, StudentSecond, TeacherSecond
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display=['title','author','pages','price']
admin.site.register(Book,BookAdmin)

### Above shit is working  ^^^^^^^^^^^^^^^^^^^^^

class  ContactInfoSecondAdmin(admin.ModelAdmin):
    list_display=['name','email','address'] 

class StudentSecondAdmin(admin.ModelAdmin):
    list_display=['rollNo','marks']

class TeacherSecondAdmin(admin.ModelAdmin):
    list_display=['subject','salary'] 

# admin.site.register(Book,BookAdmin)
admin.site.register(ContactInfoSecond,ContactInfoSecondAdmin)
# # admin.site.register(Book,StudentSecondAdmin)
# # admin.site.register(Book,TeacherSecondAdmin)
# # admin.site.register(Book)
# # admin.site.register(ContactInfo2)
admin.site.register(StudentSecond,StudentSecondAdmin)
admin.site.register(TeacherSecond,TeacherSecondAdmin)