from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count, Q
from datetime import date, timedelta

from .models import Employee, Department, Attendance, Performance
from .serializers import EmployeeSerializer, DepartmentSerializer, AttendanceSerializer, PerformanceSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [AllowAny]  # Changed for testing
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name', 'description']

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.select_related('department').all()
    serializer_class = EmployeeSerializer
    permission_classes = [AllowAny]  # Changed for testing
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['department__name', 'status', 'gender']
    search_fields = ['name', 'employee_id', 'email', 'position']
    ordering_fields = ['name', 'date_of_joining', 'salary']
    ordering = ['employee_id']
    
    @action(detail=False, methods=['get'])
    def statistics(self, request):
        total_employees = self.queryset.count()
        active_employees = self.queryset.filter(status='active').count()
        departments = Department.objects.annotate(
            employee_count=Count('employees')
        ).values('name', 'employee_count')
        
        return Response({
            'total_employees': total_employees,
            'active_employees': active_employees,
            'inactive_employees': total_employees - active_employees,
            'departments': list(departments)
        })

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.select_related('employee').all()
    serializer_class = AttendanceSerializer
    permission_classes = [AllowAny]  # Changed for testing
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['date', 'status', 'employee__name', 'employee__department__name']
    ordering_fields = ['date', 'check_in_time']
    ordering = ['-date']
    
    @action(detail=False, methods=['get'])
    def today_attendance(self, request):
        today = date.today()
        attendances = self.queryset.filter(date=today)
        serializer = self.get_serializer(attendances, many=True)
        return Response(serializer.data)

class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.select_related('employee').all()
    serializer_class = PerformanceSerializer
    permission_classes = [AllowAny]  # Changed for testing
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['rating', 'review_date', 'employee__name', 'employee__department__name']
    ordering_fields = ['review_date', 'rating']
    ordering = ['-review_date']
