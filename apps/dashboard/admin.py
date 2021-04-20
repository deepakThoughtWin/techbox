from django.contrib import admin
from .models import Category,Asset,Employee,Designation,AssignAsset
admin.site.register(AssignAsset)
admin.site.register(Category)
admin.site.register(Asset)
admin.site.register(Employee)
admin.site.register(Designation)

