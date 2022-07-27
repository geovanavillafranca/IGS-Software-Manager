from django.db import models

from .department import Department

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=120, blank=False, null=False)
    email = models.EmailField(max_length=80, blank=False, null=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
