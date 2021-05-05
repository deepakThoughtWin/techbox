from django.urls import path
from . import views

app_name = "pay"


urlpatterns = [
    path('pay/', views.index, name="pay"),
    path('charge/', views.charge, name="charge"),
    path('success/', views.successMsg, name="success"),
]
