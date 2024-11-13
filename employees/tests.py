# tests.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Employee, Contract

class EmployeeTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('admin', 'admin@example.com', 'password')
        self.employee = Employee.objects.create(
            user=self.user,
            first_name="Jan",
            last_name="Kowalski",
            email="jan.k@example.com",
            position="Manager",
            hire_date="2023-01-01"
        )

    def test_employee_list_view(self):
        self.client.login(username='admin', password='password')
        response = self.client.get(reverse('employees:employee_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Jan Kowalski")

    def test_employee_detail_view(self):
        self.client.login(username='admin', password='password')
        response = self.client.get(reverse('employees:employee_detail', args=[self.employee.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Manager")

    def test_generate_contract_view(self):
        self.client.login(username='admin', password='password')
        response = self.client.post(reverse('employees:generate_contract', args=[self.employee.pk]), {
            'template': 'sample_template.docx'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Contract.objects.filter(employee=self.employee).exists())

    def test_delete_contract_view(self):
        self.client.login(username='admin', password='password')
        contract = Contract.objects.create(employee=self.employee, document_name="Test Contract")
        response = self.client.post(reverse('employees:delete_contract', args=[contract.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Contract.objects.filter(pk=contract.pk).exists())
