from django.db import models

# Create your models here.
from django.db import models

class Student(models.Model):
    student_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    group = models.CharField(max_length=50)
    session = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name
    

class Teacher(models.Model):
    teacher_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=50, default='Lecturer')
    subject = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name
    

class Subject(models.Model):
    subject_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)

    def __str__(self):
        return self.name