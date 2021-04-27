from django.test import TestCase, Client
from django.urls import reverse
# from apps.dashboard.models import Employee
import json

class TestEmployeeViews(TestCase):
    def test_employee_view_GET(self):
        client = Client()
        client.post(reverse('login'), {'username': 'admin', 'password': '123'})
        response = client.get(reverse('dashboard:view_employee'),follow=True)
        self.assertEqual(response.status_code,200)
        # self.assertTemplateUsed(response,'dashboard/employee_list.html')
