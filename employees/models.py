from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    date_of_joining = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')

    def __str__(self):
        return self.name
    
class Attendance(models.Model):
    STATUS_CHOICES = [
        ('P', 'Present'),
        ('A', 'Absent'),
        ('L', 'Late'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='attendances')
    date = models.DateField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.employee.name} - {self.date} - {self.get_status_display()}"


class Performance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='performance_reviews')
    rating = models.IntegerField()  # 1 to 5
    review_date = models.DateField()

    def __str__(self):
        return f"{self.employee.name} - {self.rating}"
