from urllib import response
from django.shortcuts import render

from django.http import HttpResponse

import requests

# Create your views here.

url_api = 'http://127.0.0.1:8081/'


def home(request):
    return render(request, 'index.html')

def employees(request):
    url = url_api+'employees-list/'
    response = requests.get(url)
    employees = response.json()
    return render(request, 'employees.html', {'employees': employees})


def departments(request):
    url = url_api+'departments'
    response = requests.get(url)
    departments = response.json()
    return render(request, 'department.html', {'departments': departments})

