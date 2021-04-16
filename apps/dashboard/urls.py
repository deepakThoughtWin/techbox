
from django.urls import path
from . import views
# app_name = "dashboard"

urlpatterns = [
    path('home/',views.IndexView.as_view(),name='home'),
    path('employee/', views.CreateEmployeeView.as_view(), name='employee'),
    path('view_employee/', views.EmployeeView.as_view(), name='view_employee'),

]
