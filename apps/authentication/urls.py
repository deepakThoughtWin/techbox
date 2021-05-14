from . import views
from . import api_views
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path('', auth_views.LoginView.as_view(), name='login'),
    path('api/login/', api_views.LoginApiView.as_view(), name='api_login'),
    path('api/logout/', api_views.LogoutApiView.as_view(), name='api_logout'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.Registration.as_view(), name='register'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('api/user', api_views.UserApiView.as_view(),name="user_api"),
    path('api/user/<int:pk>', api_views.UserApiView.as_view(),name="user_api"),
    path('api/register/', api_views.RegisterView.as_view(), name='user_register'),
]
