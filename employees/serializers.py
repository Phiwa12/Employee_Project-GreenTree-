from rest_framework import serializers
from .models import Employee, Department, Attendance, Performance

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    department_id = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(), source='department', write_only=True
    )
    
    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'phone_number', 'address', 'date_of_joining', 'department', 'department_id']

class AttendanceSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)
    employee_id = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all(), source='employee', write_only=True
    )

    class Meta:
        model = Attendance
        fields = ['id', 'employee', 'employee_id', 'date', 'status']

class PerformanceSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)
    employee_id = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all(), source='employee', write_only=True
    )

    class Meta:
        model = Performance
        fields = ['id', 'employee', 'employee_id', 'rating', 'review_date']
