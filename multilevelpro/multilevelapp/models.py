from django.db import models

class Customer(models.Model):
    cno=models.IntegerField()
    cname=models.CharField(max_length=100)
    sales=models.IntegerField()

class Emp(Customer):
    eno=models.IntegerField()
    ename=models.CharField(max_length=100)
    salary=models.IntegerField()

class Student(Emp):
    sno=models.IntegerField()
    sname=models.CharField(max_length=100)
    marks=models.IntegerField()
