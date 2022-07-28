from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.test import APIRequestFactory
from django.test import TestCase

from .models.department import Department
from .models.employee import Employee


from .views import EmployeesViewSet
from .serializers import EmployeeSerializer, DepartmentSerializer

# Create your tests here.

class EmployeeViewSetTestCase(TestCase):
    def setUp(self):
        self.url = '/employees/'
        self.factory = APIRequestFactory()

        self.department = Department.objects.create(name='test')

    def test_empty_employee_list(self):
        view = EmployeesViewSet.as_view({'get': 'list'})
        request = self.factory.get(self.url)
        response = view(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])

    def test_create_employee(self):
        view = EmployeesViewSet.as_view({'post': 'create'})
        employee = {'name': 'je', 'email': 'je@igs-software.com.br', 'department': self.department.id}

        request = self.factory.post(self.url, data=employee)
        response = view(request)

        expected_response = EmployeeSerializer(Employee.objects.first(), many=False).data
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, expected_response)

    def test_update_employee(self):
        view = EmployeesViewSet.as_view({'post': 'create'})
        employee = {'name': 'test', 'email': 'test@igs-software.com.br', 'department': self.department.id}

        request = self.factory.post(self.url, data=employee)
        response = view(request)

        employee_data = Employee.objects.first()

        expected_response = EmployeeSerializer(employee_data, many=False).data
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, expected_response)

        view_update = EmployeesViewSet.as_view({'put':'update'})
        updated_employee = {'name': 'update name'}

        request = self.factory.put(f'{self.url}/{employee_data.id}', data=updated_employee)
        response = view_update(request, **{'pk': employee_data.id})

        expected_response_update = EmployeeSerializer(Employee.objects.first(), many=False).data

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, expected_response_update)

    
    def test_delete_employee(self):
        view = EmployeesViewSet.as_view({'post': 'create'})

        employee = {'name': 'test', 'email': 'test@igs-software.com.br', 'department': self.department.id}

        request = self.factory.post(self.url, data=employee)
        response = view(request)

        expected_response = EmployeeSerializer(Employee.objects.first(), many=False).data

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, expected_response)
        
        employee_data = Employee.objects.first()

        view_delete = EmployeesViewSet.as_view({'delete': 'destroy'})

        request = self.factory.delete(f'{self.url}/{employee_data.id}')
        response = view_delete(request, **{'pk': employee_data.id})

        expected_response_deleted = Employee.objects.first()

        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.data, expected_response_deleted)

