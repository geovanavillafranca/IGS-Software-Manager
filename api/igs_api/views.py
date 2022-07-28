from rest_framework import viewsets, generics
from rest_framework.response import Response
from .models.employee import Employee, Department


from .serializers import EmployeeSerializer, DepartmentSerializer, EmployeeListSerializer

# Create your views here.

class EmployeesViewSet(viewsets.ModelViewSet):
    """
    Return all employees
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def list(self, request, *args, **kwargs):

        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = EmployeeListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = EmployeeListSerializer(self.queryset, many=True)
        return Response(serializer.data)


class DepartmentsViewSet(viewsets.ModelViewSet):
    """
    Return all Departments
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class EmployeesListSViewSet(generics.ListAPIView):
    """
    Return all employees with department name
    """
    queryset = Employee.objects.all()
    http_method_names = ['get']
    serializer_class = EmployeeListSerializer
