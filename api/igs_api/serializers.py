from rest_framework import serializers

from .models.validator import validate_email

from .models.employee import Employee, Department

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'

    def validate(self, data):
        if not validate_email(data['email']):
            raise serializers.ValidationError({'email': "Email must follow the pattern: email@igs-software.com.br"})

        return data


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class EmployeeListSerializer(serializers.ModelSerializer):
    department = serializers.ReadOnlyField(source='department.name')

    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'department', ]


class ListAllDepartmentEmployeesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Employee
        fields = '__all__'



