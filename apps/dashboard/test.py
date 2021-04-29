from django.test import TestCase, Client
from django.urls import reverse
from apps.dashboard.models import Asset, Employee
from rest_framework.test import APIClient
from rest_framework import status

# class TestEmployeeViews(TestCase):
#     def test_employee_view_GET(self):
#         client = Client()
#         response = client.get(reverse('dashboard:view_employee'))
#         self.assertEqual(response.status_code,200)
#         # self.assertTemplateUsed(response,'dashboard/employee_list.html')


class ViewEmployeeTestCase(TestCase):
    def setUp(self):
        # """Define the test client and other test variables."""
        self.client = APIClient()
        self.designation_data={'name':'ROR'}
        self.employee_data = {"id":1,"name": "Deepak Patidar","email": "mdipakpatidar@gmail.com","phone": "7415597914","address": "Dayanand colony Nagda jn Dist. Ujjain","created_on": "2021-04-26T11:54:43.277661+05:30", "designation": 1}
        self.response = self.client.post(
            reverse('dashboard:api_designation_create'),
            self.designation_data,
            format="json")
        self.response = self.client.post(
            reverse('dashboard:api_employee_create'),
            self.employee_data,
            format="json")

    def test_01_api_can_create_a_employeelist(self):
    #     """Test the api has employee creation capability."""
        response=self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        


    def test_02_api_can_get_a_employeelist(self):
        # """Test the api can get a given bucketlist."""
        employeelist = Employee.objects.last()
        response = self.client.get(reverse('dashboard:api_employee_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, employeelist)

    def test_03_api_can_update_employeelist(self):
        employeelist = Employee.objects.last()
        self.employee_data = {"id":1,"name": "DeepakPatidar","email": "mdipakpatidar@gmail.com","phone": "07415597914","address": "Dayanand colony Nagda jn Dist. Ujjain","created_on": "2021-04-26T11:54:43.277661+05:30", "designation": 1}
        response = self.client.put(
            reverse('dashboard:api_employee_update', kwargs={'pk':employeelist.id}),self.employee_data,
             format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_04_api_can_delete_employeelist(self):
        employeelist = Employee.objects.last()
        response = self.client.delete(
            reverse('dashboard:api_employee_delete', kwargs={'pk':employeelist.id}),
             format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

# --------------------------------------Asset-------------------------------------------------
class ViewAssetTestCase(TestCase):
    def setUp(self):
        # """Define the test client and other test variables."""
        self.client = APIClient()
        self.category_data={'name':'Electronics'}
        self.asset_data = {"id":1,"name": "pendrive","model_number": "ms-2001","category": 1}
        self.response = self.client.post(
            reverse('dashboard:api_category_create'),
            self.category_data,
            format="json")
        self.response = self.client.post(
            reverse('dashboard:api_asset_create'),
            self.asset_data,
            format="json")

    def test_01_api_can_create_a_assetlist(self):
    #     """Test the api has employee creation capability."""
        response=self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        


    def test_02_api_can_get_a_assetlist(self):
        # """Test the api can get a given bucketlist."""
        assetlist = Asset.objects.last()
        response = self.client.get(reverse('dashboard:api_asset_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        

    def test_03_api_can_update_assetlist(self):
        assetlist = Asset.objects.last()
        print(assetlist.id)
        self.asset_data = {"id":1,"name": "pendrive","model_number": "ms-2001","category": 1}
        response = self.client.put(
            reverse('dashboard:api_asset_update', kwargs={'pk':assetlist.id}),self.asset_data,
             format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_04_api_can_delete_assetlist(self):
        assetlist = Asset.objects.last()
        response = self.client.delete(
            reverse('dashboard:api_asset_delete', kwargs={'pk':assetlist.id}),
             format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

# ----------------------------------------AssignAsset---------------------------------------------
class ViewAssetAssignTestCase(TestCase):
    def setUp(self):
        # """Define the test client and other test variables."""
        self.client = APIClient()
        self.designation_data={'name':'ROR'}
        self.employee_data = {"id":22,"name": "Deepak Patidar","email": "mdipakpatidar@gmail.com","phone": "7415597914","address": "Dayanand colony Nagda jn Dist. Ujjain","created_on": "2021-04-26T11:54:43.277661+05:30", "designation": 1}
        self.category_data={'name':'Electronics'}
        self.asset_data = {"id":22,"name": "pendrive","model_number": "ms-2001","category": 1}

    #     self.asset_assign_data ={
    #     "expire_on": "2021-04-23T00:00:00+05:30",
    #     "employee": 22,
    #     "asset": 22
    # },
        self.response = self.client.post(
            reverse('dashboard:api_designation_create'),
            self.designation_data,
            format="json")
        self.response = self.client.post(
            reverse('dashboard:api_employee_create'),
            self.employee_data,
            format="json")
        self.response = self.client.post(
            reverse('dashboard:api_category_create'),
            self.category_data,
            format="json")
        self.response = self.client.post(
            reverse('dashboard:api_asset_create'),
            self.asset_data,
            format="json")
        self.response = self.client.post(
            reverse('dashboard:api_borrow_asset1'),
            self.asset_assign_data,
            format="json")
        
    def test_01_api_can_create_a_assetlist(self):
    #     """Test the api has employee creation capability."""
        response=self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        


    # def test_02_api_can_get_a_assetlist(self):
    #     # """Test the api can get a given bucketlist."""
    #     assetlist = Asset.objects.last()
    #     response = self.client.get(reverse('dashboard:api_asset_list'))
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
        

    # def test_03_api_can_update_assetlist(self):
    #     assetlist = Asset.objects.last()
    #     print(assetlist.id)
    #     self.asset_data = {"id":1,"name": "pendrive","model_number": "ms-2001","category": 1}
    #     response = self.client.put(
    #         reverse('dashboard:api_asset_update', kwargs={'pk':assetlist.id}),self.asset_data,
    #          format='json'
    #     )
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_04_api_can_delete_assetlist(self):
    #     assetlist = Asset.objects.last()
    #     response = self.client.delete(
    #         reverse('dashboard:api_asset_delete', kwargs={'pk':assetlist.id}),
    #          format='json'
    #     )
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)






    # def test_02_webview_unathorized(self):
    #     data = {"name": "Deepak Patidar","email": "mdipakpatidar@gmail.com","phone": "7415597914","address": "Dayanand colony Nagda jn Dist. Ujjain", "designation": 1}
    #     headers = {}
    #     endpoint = reverse('dashboard:api_employee_create')
    #     response = self.client.post(endpoint, data=data, format='json',  **headers)
    #     self.assertEqual(response.status_code, 201)

    # def test_03_webview_unathorized(self):
    #     data = {"name": "Deepak Patidar","email": "mdipakpatidar@gmail.com","phone": "07415597914","address": "Dayanand colony Nagda jn Dist. Ujjain", "designation": 1}
    #     headers = {}
    #     endpoint = reverse('dashboard:api_category_create')
    #     response = self.client.post(endpoint, data=data, format='json',  **headers)
    #     self.assertEqual(response.status_code, 201)