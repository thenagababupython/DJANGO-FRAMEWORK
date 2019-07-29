from django.contrib import admin
from .models import Customer,Emp,Location,Student

# Register your models here.

class AdminCustomer(admin.ModelAdmin):
    list_display = ['cname','sales']

class AdminEmp(admin.ModelAdmin):
    list_display = ['ename','salary']

class AdminLocation(admin.ModelAdmin):
    list_display = ['lname','pin']

class AdminStudent(admin.ModelAdmin):
    list_display = ['sname','marks','naga']

admin.site.register(Customer,AdminCustomer)
admin.site.register(Emp,AdminEmp)
admin.site.register(Location,AdminLocation)
admin.site.register(Student,AdminStudent)
