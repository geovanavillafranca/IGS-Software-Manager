from rest_framework import serializers

from .models.validator import validate_email

from .models.employee import Employee, Department


class EmployeeSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[validate_email], required=False)
    department = serializers.CharField(required=False)

    class Meta:
        model = Employee
        fields = '__all__'
    
    def create(self, validate_data):
        validate_data['department_id'] = validate_data['department']
        del validate_data['department']
        return Employee.objects.create(**validate_data)


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class EmployeeListSerializer(serializers.ModelSerializer):
    department = serializers.ReadOnlyField(source='department.name')

    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'department', ]
