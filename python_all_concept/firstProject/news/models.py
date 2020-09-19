from django.db import models

class StudentsTable(models.Model):
    name = models.CharField(max_length=30)
    marks = models.IntegerField()
    studentAddr = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class TeacherTable(models.Model):
    name= models.CharField(max_length=30,default='demo')
    teachRatings = models.CharField(max_length=30,default=23)


# whenever we are trying to print emp object internally it will called __str__ method and return the name 
