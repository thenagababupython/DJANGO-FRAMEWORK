from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model):
    # student=models.ForeignKey(Student,on_delete=models.DO_NOTHING)
    # student=models.ForeignKey(Student,on_delete=models.SET_NULL,null=True)
    student=models.ManyToManyField(Student)
    cname=models.CharField(max_length=100)
    cost=models.IntegerField()

    def __str__(self):
        return self.cname
