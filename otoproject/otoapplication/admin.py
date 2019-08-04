from django.contrib import admin
from .models import Student,Courses
# Register your models here.

class AdminStudent(admin.ModelAdmin):
    list_display = ['name','email','location']

class AdminCourses(admin.ModelAdmin):
    list_display = ['cname','cost']

admin.site.register(Student,AdminStudent)
admin.site.register(Courses,AdminCourses)
