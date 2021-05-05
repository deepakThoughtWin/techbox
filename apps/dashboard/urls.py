from django.urls import path
from apps.dashboard import views
from apps.dashboard import api_views

app_name = "dashboard"

urlpatterns = [
    path('home/',views.IndexView.as_view(),name='home'),
    
    path('test', views.HomePageView.as_view(), name='test'),
    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session),
    # path('success/', views.SuccessView.as_view()), # new
    path('cancelled/', views.CancelledView.as_view()),

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



# API----------------------------API-------------------------------------------------------------
# ------------------------------Employee-------------------------------------------------------
    path('api/employee/create',api_views.EmployeeCreateApi.as_view(),name='api_employee_create'),
    path('api/employee/list',api_views.EmployeeListApi.as_view(),name='api_employee_list'),
    path('api/employee/update/<int:pk>',api_views.EmployeeUpdateApi.as_view(),name='api_employee_update'),
    path('api/employee/delete/<int:pk>',api_views.EmployeeDeleteApi.as_view(),name='api_employee_delete'),

# --------------------------------Designation-------------------------------------------------------
    path('api/designation/create',api_views.DesignationCreateApi.as_view(),name='api_designation_create'),

    path('api/designation/list',api_views.DesignationListApi.as_view(),name='api_designation_list'),
    path('api/designation/update/<int:pk>',api_views.DesignationUpdateApi.as_view(),name='api_designation_update'),

    path('api/designation/delete/<int:pk>',api_views.DesignationDeleteApi.as_view(),name='api_designation_delete'),

# --------------------------------asset-------------------------------------------------------
    path('api/asset/create',api_views.AssetCreateApi.as_view(),name='api_asset_create'),

    path('api/asset/list',api_views.AssetListApi.as_view(),name='api_asset_list'),
    path('api/asset/update/<int:pk>',api_views.AssetUpdateApi.as_view(),name='api_asset_update'),

    path('api/asset/delete/<int:pk>',api_views.AssetDeleteApi.as_view(),name='api_asset_delete'),

# --------------------------------category-------------------------------------------------------
    path('api/category/create',api_views.CategoryCreateApi.as_view(),name='api_category_create'),

    path('api/category/list',api_views.CategoryListApi.as_view(),name='api_category_list'),
    path('api/category/update/<int:pk>',api_views.CategoryUpdateApi.as_view(),name='api_category_update'),

    path('api/category/delete/<int:pk>',api_views.CategorytDeleteApi.as_view(),name='api_category_delete'),

# ------------------------------assignasset--------------------------------------------------------
    path('api/borrowasset/<int:pk>',api_views.AssignAssetDetailAPI.as_view(),name='api_borrow_asset'),
    path('api/borrowasset/',api_views.AssignAssetDetailAPI.as_view(),name='api_borrow_asset1'),
]
 