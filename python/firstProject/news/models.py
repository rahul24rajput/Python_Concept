from django.db import models

class StudentsTable(models.Model):
    name = models.CharField(max_length=30)
    marks = models.IntegerField()
    studentAddr = models.CharField(max_length=30)
    

