from rest_framework import  serializers
from .models import Asset, AssignAsset, Category, Employee,Designation

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        # fields = '__all__'
        exclude =('status',)

class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = '__all__'
        # exclude =('status',)

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        # fields = '__all__'
        exclude =('availability',)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        # exclude =('status',)


class AssignAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignAsset
        fields = '__all__'
        # exclude =('release',)
