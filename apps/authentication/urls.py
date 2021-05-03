from . import views
from . import api_views

from django.contrib.auth import views as auth_views
from django.urls import path
urlpatterns = [
    path('', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.Registration.as_view(), name='register'), 
    path('profile/', views.ProfileView.as_view(), name='profile'), 
    path('user_list', api_views.UserListView.as_view(),name="user_list"),
]