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
    model_number = models.CharField(max_length=100)
    availability =models.BooleanField(default=True)
    added_date = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
