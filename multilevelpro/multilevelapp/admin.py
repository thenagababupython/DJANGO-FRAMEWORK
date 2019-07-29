from django.contrib import admin

from .models import Customer,Emp,Student

class AdminCustomer(admin.ModelAdmin):
    list_display = ['cno','cname','sales']

class AdminEmp(admin.ModelAdmin):
    list_display = ['eno','ename','salary']

class AdminStudent(admin.ModelAdmin):
    list_display = ['sno','sname','marks']



admin.site.register(Customer,AdminCustomer)
admin.site.register(Emp,AdminEmp)
admin.site.register(Student,AdminStudent)