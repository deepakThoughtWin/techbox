from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Category,Asset,Employee,Designation,AssignAsset


@admin.register(Employee)
class EmployeeAdmin(ImportExportModelAdmin):
    pass
     
@admin.register(Asset)
class AssetAdmin(ImportExportModelAdmin):
    pass

admin.site.register(AssignAsset)
admin.site.register(Category)
admin.site.register(Designation)

