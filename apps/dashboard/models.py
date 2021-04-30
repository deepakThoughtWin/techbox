from django.db import models

class AssignAsset(models.Model):
    employee=models.ForeignKey('Employee',on_delete=models.CASCADE)
    asset=models.ForeignKey('Asset',on_delete=models.CASCADE)
    assign_on=models.DateTimeField(auto_now_add=True)
    expire_on = models.DateTimeField()
    release =models.BooleanField(default=True)
    release_on = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.employee.name +"-"+ self.asset.name

    class Meta:
        ordering = ['-release_on']

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
    added_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name 
    class Meta:
        ordering = ['-added_on']

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True,editable=True)
    designation = models.ForeignKey('Designation',on_delete=models.CASCADE)
    phone =models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    status =models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return  self.email

class Designation(models.Model):
    name = models.CharField(max_length=100)
    created_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
