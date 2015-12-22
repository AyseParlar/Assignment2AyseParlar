from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    courses = models.ManyToManyField('Course', related_name='students')


class Course(models.Model):
    teacher = models.ForeignKey('Teacher')
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    classroom = models.CharField(max_length=10)
    times = models.TextField()


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    office_details = models.TextField()
    phone = models.CharField(max_length=100)
    email = models.EmailField()
