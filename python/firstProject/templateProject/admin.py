from django.contrib import admin

# Register your models here.
from templateProject.models import EmpRevised

class EmpRevisedAdmin(admin.ModelAdmin):
    list_display=['name','rollno']

admin.site.register(EmpRevised,EmpRevisedAdmin)
