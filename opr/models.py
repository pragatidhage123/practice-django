from django.db import models

# Create your models here.

class Student(models.Model):

    roll_number = models.IntegerField()
    first_name = models.CharField(max_length=255,default="unknow")
    last_name = models.CharField(max_length=200,null=True)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name

class Teacher(models.Model):

    first_name = models.CharField(max_length=255,default="unknow")
    last_name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name

