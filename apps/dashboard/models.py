from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Asset(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    model_number = models.CharField(max_length=100,null=True,blank=True)
    availability =models.BooleanField(default=True)
    added_date = models.DateTimeField(auto_now=True)
    expire_date=models.DateTimeField()
    employee=models.ForeignKey('Employee',on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    designation = models.ForeignKey('Designation',on_delete=models.CASCADE)
    phone =models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    status =models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Designation(models.Model):
    name = models.CharField(max_length=100)
    created_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name