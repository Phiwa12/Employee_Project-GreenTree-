from django.core.management.base import BaseCommand
from employees.models import Employee, Department, Attendance, Performance
from faker import Faker
import random

fake = Faker()

class Command(BaseCommand):
    help = 'Seed the database with fake employees, attendance and performance'

    def handle(self, *args, **kwargs):
        departments = ['HR', 'Engineering', 'Marketing', 'Sales', 'Finance']
        department_objs = []

        for dept_name in departments:
            dept, _ = Department.objects.get_or_create(name=dept_name)

            department_objs.append(dept)

        for _ in range(50):
            department = random.choice(department_objs)
            employee = Employee.objects.create(
                name=fake.name(),
                email=fake.email(),
                phone_number=fake.phone_number(),
                address=fake.address(),
                date_of_joining=fake.date_between(start_date='-2y', end_date='today'),
                department=department
            )

            for _ in range(5):
                Attendance.objects.create(
                    employee=employee,
                    date=fake.date_between(start_date='-30d', end_date='today'),
                    status=random.choice(['Present', 'Absent', 'Late'])
                )

            for _ in range(2):
                Performance.objects.create(
                    employee=employee,
                    rating=random.randint(1, 5),
                    review_date=fake.date_between(start_date='-1y', end_date='today')
                )

        self.stdout.write(self.style.SUCCESS('✅ Successfully seeded fake data.'))
