from django.db import models

# Create your models here.
class Customer(models.Model):
    cid=models.AutoField(primary_key=True)
    cname=models.CharField(max_length=100)
    sales=models.IntegerField()

class Emp(models.Model):
    eid=models.AutoField(primary_key=True)
    ename=models.CharField(max_length=100)
    salary=models.IntegerField()


class Location(models.Model):
    lid=models.AutoField(primary_key=True)
    lname=models.CharField(max_length=100)
    pin=models.IntegerField()

class Student(Customer,Emp,Location):
    id=models.AutoField(primary_key=True)
    sname=models.CharField(max_length=100)
    marks=models.IntegerField()
