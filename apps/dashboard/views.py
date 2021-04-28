
from typing import Generic
from django import views
from django.db.models import query
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic,View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from apps.dashboard.forms import AssetForm, AssignAssetForm, EmployeeForm,DesignationForm,AssetUpdateForm,CategoryForm
from apps.dashboard.models import Asset, AssignAsset, Category, Designation, Employee
from django.urls import reverse_lazy
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from datetime import datetime, timedelta
from django.utils import timezone
from .task import borrow_mail, send_notification_expire

class IndexView(generic.ListView):
    template_name = "dashboard/index.html"
    queryset =Employee.objects.all()
    queryset1=Asset.objects.all()
    queryset2=AssignAsset.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_employee'] = self.queryset.all().count()
        context['total_asset'] = self.queryset1.all().count()
        context['assign_asset_list'] = self.queryset2.filter(expire_on__lte=datetime.now().date(),release=True)
        context['total_assign_asset_expired'] = self.queryset2.filter(expire_on__lte=datetime.now().date(),release=True).count()
        context['total_assign_asset'] = self.queryset2.filter(release=True).count()
        send_notification_expire.delay()
        return context

@method_decorator(login_required, name='dispatch')
class CreateEmployeeView(SuccessMessageMixin,generic.CreateView):
    form_class = EmployeeForm
    model = Employee
    template_name = "dashboard/create_employee.html"
    success_url = reverse_lazy('dashboard:view_employee')
    success_message = "Employee was Created successfully"
    # def form_valid(self, form):
    #     obj = form.save(commit=False)
    #     obj.author = self.request.user
    #     return super(CreatePostView, self).form_valid(form)

@method_decorator(login_required, name='dispatch')
class EmployeeView(generic.ListView):
    template_name="dashboard/employee_list.html"
    def get_queryset(self):
        return Employee.objects.all()

@method_decorator(login_required, name='dispatch')
class EmployeeDeleteView(SuccessMessageMixin,generic.DeleteView):
    model = Employee
    success_url = reverse_lazy('dashboard:view_employee')
    success_message = "Employee was Deleted successfully"   
    def get(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return self.delete(request, *args, **kwargs)

@method_decorator(login_required, name='dispatch')
class UpdateEmployeeView(SuccessMessageMixin,generic.UpdateView):
    form_class = EmployeeForm
    model = Employee
    template_name = "dashboard/update_employee.html"
    success_url = reverse_lazy('dashboard:view_employee')
    success_message = "Employee was Updated successfully"


    
@method_decorator(login_required, name='dispatch')
class DesignationView(generic.ListView):
    template_name="dashboard/designation_list.html"
    def get_queryset(self):
        return Designation.objects.all()

@method_decorator(login_required, name='dispatch')
class CreateDesignationView(SuccessMessageMixin,generic.CreateView):
    form_class = DesignationForm
    model = Designation
    template_name = "dashboard/create_designation.html"
    success_url = reverse_lazy('dashboard:view_designation')
    success_message = "Designation was Created successfully"

@method_decorator(login_required, name='dispatch')
class DesignationDeleteView(SuccessMessageMixin,generic.DeleteView):
    model = Designation
    success_message = "Designation was Deleted successfully"

    success_url = reverse_lazy('dashboard:view_designation')
    def get(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return self.delete(request, *args, **kwargs)

@method_decorator(login_required, name='dispatch')
class UpdateDesignationView(SuccessMessageMixin,generic.UpdateView):
    form_class = DesignationForm
    model = Designation
    template_name = "dashboard/update_designation.html"
    success_url = reverse_lazy('dashboard:view_designation')
    success_message = "Designation was Updated successfully"



@method_decorator(login_required, name='dispatch')
class CreateAssetView(SuccessMessageMixin,generic.CreateView):
    form_class = AssetForm
    model = Asset
    template_name = "dashboard/create_asset.html"
    success_url = reverse_lazy('dashboard:view_asset')
    success_message = "Asset was Created successfully"


@method_decorator(login_required, name='dispatch')
class AssetView(generic.ListView):
    template_name="dashboard/asset_list.html"
    def get_queryset(self):
        return Asset.objects.all()

@method_decorator(login_required, name='dispatch')
class AssetDeleteView(SuccessMessageMixin,generic.DeleteView):
    model = Asset
    success_message = "Asset was Deleted successfully"
    success_url = reverse_lazy('dashboard:view_asset')
    def get(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return self.delete(request, *args, **kwargs)

@method_decorator(login_required, name='dispatch')
class UpdateAssetView(SuccessMessageMixin,generic.UpdateView):
    form_class = AssetUpdateForm
    model = Asset
    template_name = "dashboard/update_asset.html"
    success_url = reverse_lazy('dashboard:view_asset')
    success_message = "Asset was Updated successfully"


@method_decorator(login_required, name='dispatch')
class CreateCategoryView(SuccessMessageMixin,generic.CreateView):
    form_class = CategoryForm
    model = Category
    template_name = "dashboard/create_category.html"
    success_url = reverse_lazy('dashboard:view_category')
    success_message = "Category was Created successfully"




@method_decorator(login_required, name='dispatch')
class CategoryView(generic.ListView):
    template_name="dashboard/category_list.html"
    def get_queryset(self):
        return Category.objects.all()

@method_decorator(login_required, name='dispatch')
class CategoryDeleteView(SuccessMessageMixin,generic.DeleteView):
    model = Category
    success_message = "Category was Deleted successfully"
    success_url = reverse_lazy('dashboard:view_category')
    def get(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return self.delete(request, *args, **kwargs)

@method_decorator(login_required, name='dispatch')
class UpdateCategoryView(SuccessMessageMixin,generic.UpdateView):
    form_class = CategoryForm
    model = Category
    template_name = "dashboard/update_category.html"
    success_url = reverse_lazy('dashboard:view_category')
    success_message = "Category was Updated successfully"



class AssignAssetView(View):
    def get(self, request, *args, **kwargs):
        form = AssignAssetForm()
        return render(request,'dashboard/assign_asset.html',{'form':form})

    def post(self, request, *args, **kwargs):
        form = AssignAssetForm(request.POST or None)
        if form.is_valid():
            email_return= form.cleaned_data['employee']
            asset= form.cleaned_data['asset']
            expire= form.cleaned_data['expire_on']
            object=form.save(commit=False)
            employee=Employee.objects.get(email=email_return)
            name=employee.name
            email=employee.email
            print(name)
            object.release=True
            object.save()
            messages.success(self.request,f"{asset} borrowed by {employee} Successfully ")
            email= form.cleaned_data['employee']
            mail_list=[email,]
            borrow_mail.delay(mail_list,asset,expire,name)
        return HttpResponseRedirect("/view_assign_asset")


class ReleaseAssetView(View):
    def get(self,request,id):
        queryset=AssignAsset.objects.filter(id=id).update(release=False)
        queryset1=AssignAsset.objects.filter(id=id).update(release_on=timezone.now())
        messages.success(request,"Asset Submitted Successfully")
        return HttpResponseRedirect("/view_assign_asset")

class AssignAssetListView(generic.ListView):
    model = AssignAsset
    template_name = "dashboard/assign_asset_list.html"
    queryset = AssignAsset.objects.filter(release=True)

class AssetBorrowHistory(View):
    def get(self,request,id):
        queryset=AssignAsset.objects.filter(employee__id=id)
        employee=Employee.objects.filter(id=id)
        context={}
        for employee in employee:
                context['name']=employee.name
                break
        context['queryset']=queryset
        print(context)
        return render(request,"dashboard/asset_history.html",context=context)