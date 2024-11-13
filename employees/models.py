from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Model Employee
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=100)
    hire_date = models.DateField()
    contract_downloaded = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Model Contract
class Contract(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='contracts')
    document_path = models.CharField(max_length=255)
    generated_date = models.DateTimeField(default=timezone.now)
    document_name = models.CharField(max_length=255)

    def __str__(self):
        return f"Umowa {self.document_name} dla {self.employee.first_name} {self.employee.last_name} z dnia {self.generated_date.strftime('%Y-%m-%d')}"