from django.urls import path
from apps.dashboard import views
from apps.dashboard import task

app_name = "dashboard"


urlpatterns = [
    path('home/',views.IndexView.as_view(),name='home'),
    # path('task/',task.send_notifiction,name='task'),
    path('employee/', views.CreateEmployeeView.as_view(), name='employee'),
    path('designation/', views.CreateDesignationView.as_view(), name='designation'),
    path('asset/', views.CreateAssetView.as_view(), name='asset'),
    path('category/', views.CreateCategoryView.as_view(), name='category'),
    path('assign_asset/', views.AssignAssetView.as_view(), name='assign_asset'),
    
    path('view_employee', views.EmployeeView.as_view(), name='view_employee'),
    path('view_designation', views.DesignationView.as_view(), name='view_designation'),
    path('view_asset', views.AssetView.as_view(), name='view_asset'),
    path('view_category', views.CategoryView.as_view(), name='view_category'),
    path('view_assign_asset', views.AssignAssetListView.as_view(), name='view_assign_asset'),
    

    path('delete_employee/delete/<int:pk>',views.EmployeeDeleteView.as_view(),name='delete_employee'),
    path('delete_designation/delete/<int:pk>',views.DesignationDeleteView.as_view(),name='delete_designation'),
    path('delete_asset/delete/<int:pk>',views.AssetDeleteView.as_view(),name='delete_asset'),
    path('delete_category/delete/<int:pk>',views.CategoryDeleteView.as_view(),name='delete_category'),
    
    path('release_asset/<int:id>',views.ReleaseAssetView.as_view(),name='release_asset'),
    path('asset_borrow/<int:id>',views.AssetBorrowHistory.as_view(),name='asset_borrow'),
    path('update_employee/<int:pk>',views.UpdateEmployeeView.as_view(),name='update_employee'),
    path('update_designation/<int:pk>',views.UpdateDesignationView.as_view(),name='update_designation'),
    path('update_asset/<int:pk>',views.UpdateAssetView.as_view(),name='update_asset'),
    path('update_category/<int:pk>',views.UpdateCategoryView.as_view(),name='update_category'),




]
