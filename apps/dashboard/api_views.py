from rest_framework import generics
from rest_framework.response import Response
from apps.dashboard import serializers
from .models import AssignAsset, Designation, Employee,Asset,Category
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# ----------------------------Employee-------------------------------------------
class EmployeeCreateApi(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer

class EmployeeListApi(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer

class EmployeeUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer

class EmployeeDeleteApi(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer

# -------------------------Designation----------------------------------------------------
class DesignationCreateApi(generics.CreateAPIView):
    queryset = Designation.objects.all()
    serializer_class = serializers.DesignationSerializer

class DesignationListApi(generics.ListAPIView):
    queryset = Designation.objects.all()
    serializer_class = serializers.DesignationSerializer

class DesignationUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Designation.objects.all()
    serializer_class = serializers.DesignationSerializer

class DesignationDeleteApi(generics.DestroyAPIView):
    queryset = Designation.objects.all()
    serializer_class = serializers.DesignationSerializer

# -------------------------------Asset-------------------------------------------------
class AssetCreateApi(generics.CreateAPIView):
    queryset = Asset.objects.all()
    serializer_class = serializers.AssetSerializer

class AssetListApi(generics.ListAPIView):
    queryset = Asset.objects.all()
    serializer_class = serializers.AssetSerializer

class AssetUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Asset.objects.all()
    serializer_class = serializers.AssetSerializer

class AssetDeleteApi(generics.DestroyAPIView):
    queryset = Asset.objects.all()
    serializer_class = serializers.AssetSerializer

# -------------------------------Category-------------------------------------------------
class CategoryCreateApi(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer

class CategoryListApi(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer

class CategoryUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer

class CategorytDeleteApi(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer


# -----------------------------AssignAsset------------------------------------------------

class AssignAssetDetailAPI(APIView):
    def get_object(self,pk=None):
        try:
            return AssignAsset.objects.get(pk=pk)
        except AssignAsset.DoesNotExist:
            raise Http404

    def get(self,request,pk=None,format=None):
        if pk is None:
            assignasset = AssignAsset.objects.all()
            serializer = serializers.AssignAssetSerializer(assignasset, many=True)
            return Response(serializer.data)
        else:
            assignasset=self.get_object(pk)
            serializer = serializers.AssignAssetSerializer(assignasset)
            return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer =serializers.AssignAssetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        assignasset = self.get_object(pk)
        serializer = serializers.AssignAssetSerializer(assignasset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        assignasset = self.get_object(pk)
        assignasset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

