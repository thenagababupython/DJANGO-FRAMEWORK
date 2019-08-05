from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)

    def __str__(self):
        return self.name


class Courses(models.Model):
    # abc=models.OneToOneField(Student)
    # abc=models.OneToOneField(Student,on_delete=models.DO_NOTHING)
    # abc=models.OneToOneField(Student,on_delete=models.SET_NULL,null=True)
    # abc=models.OneToOneField(Student,on_delete=models.SET(6),null=True)
    abc=models.OneToOneField(Student,on_delete=models.CASCADE,null=True)
    cname=models.CharField(max_length=100)
    cost=models.IntegerField()
