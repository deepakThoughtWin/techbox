from django.urls import path
from apps.dashboard import views

app_name = "dashboard"


urlpatterns = [
    path('home/',views.IndexView.as_view(),name='home'),
    path('employee/', views.CreateEmployeeView.as_view(), name='employee'),
    path('designation/', views.CreateDesignationView.as_view(), name='designation'),
    path('asset/', views.CreateAssetView.as_view(), name='asset'),
    
    path('view_employee', views.EmployeeView.as_view(), name='view_employee'),
    path('view_employee', views.DesignationView.as_view(), name='view_designation'),

    path('delete_employee/delete/<int:pk>',views.EmployeeDeleteView.as_view(),name='delete_employee'),
    path('delete_designation/delete/<int:pk>',views.DesignationDeleteView.as_view(),name='delete_designation'),
    
    path('update_employee/<int:pk>',views.UpdateEmployeeView.as_view(),name='update_employee'),
    path('update_designation/<int:pk>',views.UpdateDesignationView.as_view(),name='update_designation'),




]
