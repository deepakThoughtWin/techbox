from django.test import TestCase, Client
from django.urls import reverse
# from apps.dashboard.models import Employee
import json

class TestEmployeeViews(TestCase):
    def test_employee_view_GET(self):
        client = Client()
        response = client.get(reverse('dashboard:view_employee'))
        self.assertEqual(response.status_code,200)
        # self.assertTemplateUsed(response,'dashboard/employee_list.html')
