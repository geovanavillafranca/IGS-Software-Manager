from django.contrib import admin

from .models.employee import Employee
from .models.department import Department



# Register your models here.


class Employees(admin.ModelAdmin):
    list_display = ('name', 'email', 'department')
    list_display_links = ('name',)

admin.site.register(Employee, Employees)


class Departments(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)

admin.site.register(Department, Departments)
