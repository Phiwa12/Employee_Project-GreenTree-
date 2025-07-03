# Employee_Project-GreenTree-
Employee Management System

A comprehensive Django REST API application for managing employees, departments, attendance, and performance reviews with beautiful data visualizations.

Features

- **Employee Management**: CRUD operations for employees with detailed profiles
- **Department Management**: Organize employees by departments
- **Attendance Tracking**: Track daily attendance with multiple status options
- **Performance Reviews**: Manage employee performance evaluations
- **RESTful APIs**: Comprehensive API endpoints with filtering, pagination, and search
- **Interactive Charts**: Beautiful data visualizations using Chart.js
- **API Documentation**: Auto-generated Swagger/OpenAPI documentation
- **Authentication**: JWT token-based authentication
- **Admin Interface**: Django admin for easy data management

Quick Start

### Prerequisites
- Python 3.8+
- PostgreSQL
- Git

### Installation

1. Clone the repository
   ```bash
   git clone <your-repo-url>
   cd employee-management-system
   ```

2. Create virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment setup**
   ```bash
   cp .env.example .env
   # Edit .env with your database credentials
   ```

5. **Database setup**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Create superuser
   ```bash
   python manage.py createsuperuser
   ```

7. **Seed sample data**
   ```bash
   python manage.py seed_data --employees 50
   ```

8. **Run the server**
   ```bash
   python manage.py runserver
   ```

## Docker Setup (Optional)

```bash
# Build and run with docker-compose
docker-compose up --build

# Run migrations in container
docker-compose exec web python manage.py migrate

# Create superuser in container
docker-compose exec web python manage.py createsuperuser

# Seed data in container
docker-compose exec web python manage.py seed_data --employees 50
```

## API Documentation


#### Authentication
- `POST /api/token/` - Obtain JWT token
- `POST /api/token/refresh/` - Refresh JWT token

#### Employees
- `GET /api/employees/` - List all employees (with filtering, search, pagination)
- `POST /api/employees/` - Create new employee
- `GET /api/employees/{id}/` - Get employee details
- `PUT/PATCH /api/employees/{id}/` - Update employee
- `DELETE /api/employees/{id}/` - Delete employee
- `GET /api/employees/statistics/` - Get employee statistics
- `GET /api/employees/by_department/` - Group employees by department

#### Departments
- `GET /api/departments/` - List all departments
- `POST /api/departments/` - Create new department
- `GET /api/departments/{id}/` - Get department details
- `PUT/PATCH /api/departments/{id}/` - Update department
- `DELETE /api/departments/{id}/` - Delete department

#### Attendance
- `GET /api/attendance/` - List attendance records
- `POST /api/attendance/` - Create attendance record
- `GET /api/attendance/{id}/` - Get attendance details
- `PUT/PATCH /api/attendance/{id}/` - Update attendance
- `DELETE /api/attendance/{id}/` - Delete attendance
- `GET /api/attendance/monthly_report/` - Get monthly attendance report
- `GET /api/attendance/employee_attendance/` - Get employee attendance summary

#### Performance
- `GET /api/performance/` - List performance reviews
- `POST /api/performance/` - Create performance review
- `GET /api/performance/{id}/` - Get performance details
- `PUT/PATCH /api/performance/{id}/` - Update performance
- `DELETE /api/performance/{id}/` - Delete performance
- `GET /api/performance/average_ratings/` - Get average ratings by department

### API Features

#### Filtering
```bash
# Filter employees by department
GET /api/employees/?department=1

# Filter by status
GET /api/employees/?status=active

# Filter by date range
GET /api/employees/?date_joined_after=2023-01-01&date_joined_before=2023-12-31

# Filter by salary range
GET /api/employees/?salary_min=50000&salary_max=100000
```

#### Searching
```bash
# Search employees by name or email
GET /api/employees/?search=john

# Search departments
GET /api/departments/?search=engineering
```

#### Ordering
```bash
# Order by date joined (descending)
GET /api/employees/?ordering=-date_joined

# Order by salary (ascending)
GET /api/employees/?ordering=salary
```

#### Pagination
```bash
# Get specific page
GET /api/employees/?page=2

# Results include pagination info:
{
  "count": 50,
  "next": "http://localhost:8000/api/employees/?page=3",
  "previous": "http://localhost:8000/api/employees/?page=1",
  "results": [...]
}
```

## Authentication

The API uses JWT (JSON Web Token) authentication. To access protected endpoints:

1. **Obtain token**
   ```bash
   POST /api/token/
   {
     "username": "your_username",
     "password": "your_password"
   }
   ```

2. **Use token in requests**
   ```bash
   Authorization: Bearer <your_access_token>
   ```
## Project Structure
```
employee_project/
├── employees/              # Employee and department models
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── filters.py
│   ├── admin.py
│   └── management/
│       └── commands/
│           └── seed_data.py
├── attendance/             # Attendance and performance models
│   ├── models.py
├── employee_project/       # Main project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static/                 # Static files
├── requirements.txt
├── .env.example
└── README.md
```

### Running Tests
```bash
python manage.py test
```

### Code Quality
The project follows Django best practices:
- Modular app structure
- Proper model relationships
- DRY principle
- Comprehensive error handling
- API versioning ready
- Environment-based configuration

## Deployment

### Environment Variables
```bash
DEBUG=False
SECRET_KEY=your-production-secret-key
DATABASE_NAME=your_db_name
DATABASE_USER=your_db_user
DATABASE_PASSWORD=your_db_password
DATABASE_HOST=your_db_host
DATABASE_PORT=5432
```

### Production Checklist
- [ ] Set `DEBUG=False`
- [ ] Configure proper `SECRET_KEY`
- [ ] Set up production database
- [ ] Configure static files serving
- [ ] Set up HTTPS
- [ ] Configure CORS for frontend
- [ ] Set up monitoring and logging

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request


## 👥 Authors

- Phiwayinkhosi Precious Lukhele - Initial work

## 🙏 Acknowledgments

- Django community for excellent documentation
- Django REST Framework for powerful API tools
- Faker for realistic test data generation
"""

# =====================================
# 15. FINAL SETUP COMMANDS
# =====================================

# Create these files in your project:
# 1. Save all the Python code in respective files
# 2. Run these commands:

"""
# Initial setup commands:
python manage.py makemigrations employees
python manage.py makemigrations attendance
python manage.py migrate
python manage.py createsuperuser
python manage.py seed_data --employees 50
python manage.py collectstatic --noinput
python manage.py runserver

# Access points:
# - Admin: http://localhost:8000/admin/
# - API Docs: http://localhost:8000/swagger/
# - API Root: http://localhost:8000/api/
"""
