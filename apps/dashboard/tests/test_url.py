from django.test import TestCase

from django.urls import reverse,resolve

from apps.dashboard.views import CreateEmployeeView,EmployeeView,EmployeeDeleteView,UpdateEmployeeView

class TestEmployeeUrls(TestCase):
    def test_create_url_is_resolved(self):
        url =reverse('dashboard:employee')
        self.assertEqual(resolve(url).func.view_class,CreateEmployeeView )

    def test_view_url_is_resolved(self):
        url=reverse('dashboard:view_employee')
        self.assertEqual(resolve(url).func.view_class,EmployeeView )

    def test_delete_url_is_resolved(self, *args, **kwargs):
        url=reverse('dashboard:delete_employee', kwargs={'pk': 0})
        self.assertEqual(resolve(url).func.view_class,EmployeeDeleteView )

    def test_update__url_is_resolved(self, *args, **kwargs):
        url=reverse('dashboard:update_employee', kwargs={'pk': 0})
        self.assertEqual(resolve(url).func.view_class,UpdateEmployeeView )

