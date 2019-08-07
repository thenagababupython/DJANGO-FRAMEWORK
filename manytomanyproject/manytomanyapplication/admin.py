from django.contrib import admin
from.models import Student,Course

# Register your models here.


class AdminStudent(admin.ModelAdmin):
    list_display = ['name','email','location']

class AdminCourse(admin.ModelAdmin):
    list_display = ['cname','cost']

admin.site.register(Student,AdminStudent)
admin.site.register(Course,AdminCourse)