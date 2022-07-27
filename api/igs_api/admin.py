from django.contrib import admin

from .models.employee import Employee


# Register your models here.


class Employees(admin.ModelAdmin):
    list_display = ('name', 'email', 'department')
    list_display_links = ('name',)

admin.site.register(Employee, Employees)



