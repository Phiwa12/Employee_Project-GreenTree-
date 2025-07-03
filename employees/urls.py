from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, EmployeeViewSet, AttendanceViewSet, PerformanceViewSet

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'attendance', AttendanceViewSet)
router.register(r'performance', PerformanceViewSet)
#router.register(r'employees', EmployeeViewSet, basename='employee')

urlpatterns = [
    path('', include(router.urls)),
]
