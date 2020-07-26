from django.db import models
from django.urls import reverse
# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=23)
    author = models.CharField(max_length=64)
    pages = models.PositiveIntegerField()
    price = models.FloatField()

    def get_absolute_url(self):
        return reverse('bookDetail', kwargs={'pk': self.pk})

# Below topic is all about model inhertince and how to use bas model inheritence

############################################
# Base Abstract inheritence
###########################################


class ContactInfo(models.Model):
    name = models.CharField(max_length=34)
    email = models.EmailField()
    address = models.CharField(max_length=89)

    class Meta:
        abstract = True  # it is given so the table will not create in DB. The solely purpose of this
        # would be only inheritence.


class Student(ContactInfo):
    rollNo = models.IntegerField()
    marks = models.IntegerField()


class Teacher(ContactInfo):
    subject = models.CharField(max_length=36)
    salary = models.FloatField()
###########################################

# Multi table inhertince


class ContactInfoSecond(models.Model):
    name = models.CharField(max_length=34)
    email = models.EmailField()
    address = models.CharField(max_length=89)


class StudentSecond(ContactInfoSecond):
    rollNo = models.IntegerField()
    marks = models.IntegerField()


class TeacherSecond(ContactInfoSecond):
    subject = models.CharField(max_length=34)
    salary = models.FloatField()
# These all tables can be seen in admin panel
