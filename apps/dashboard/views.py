from django import views
from django.db.models import query
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic,View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from apps.dashboard.forms import AssetForm, AssignAssetForm, EmployeeForm,DesignationForm,AssetUpdateForm,CategoryForm
from apps.dashboard.models import Asset, AssignAsset, Category, Designation, Employee
from django.urls import reverse_lazy
from django.conf import settings
from django.core.mail import send_mail

class IndexView(generic.ListView):
    template_name = "dashboard/index.html"
    queryset =Employee.objects.all()
    queryset1=Asset.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_employee'] = self.queryset.all().count()
        context['total_asset'] = self.queryset1.all().count()
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
class EmployeeDeleteView(generic.DeleteView):
    model = Employee
    # template_name = 'dshboard/employee_confirm_delete.html'
    success_url = reverse_lazy('dashboard:view_employee')
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

@method_decorator(login_required, name='dispatch')
class UpdateEmployeeView(generic.UpdateView):
    form_class = EmployeeForm
    model = Employee
    template_name = "dashboard/update_employee.html"
    success_url = reverse_lazy('dashboard:view_employee')

    
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
    success_message = "Employee was Created successfully"

@method_decorator(login_required, name='dispatch')
class DesignationDeleteView(generic.DeleteView):
    model = Designation
    # Template_name = 'dashboard/designaion_confirm_delete.html'
    success_url = reverse_lazy('dashboard:view_designation')
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

@method_decorator(login_required, name='dispatch')
class UpdateDesignationView(generic.UpdateView):
    form_class = DesignationForm
    model = Designation
    template_name = "dashboard/update_designation.html"
    success_url = reverse_lazy('dashboard:view_designation')


@method_decorator(login_required, name='dispatch')
class CreateAssetView(SuccessMessageMixin,generic.CreateView):
    form_class = AssetForm
    model = Asset
    template_name = "dashboard/create_asset.html"
    success_url = reverse_lazy('dashboard:view_asset')

@method_decorator(login_required, name='dispatch')
class AssetView(generic.ListView):
    template_name="dashboard/asset_list.html"
    def get_queryset(self):
        return Asset.objects.all()

@method_decorator(login_required, name='dispatch')
class AssetDeleteView(generic.DeleteView):
    model = Asset
    # Template_name = 'dashboard/asset_confirm_delete.html'
    success_url = reverse_lazy('dashboard:view_asset')
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

@method_decorator(login_required, name='dispatch')
class UpdateAssetView(generic.UpdateView):
    form_class = AssetUpdateForm
    model = Asset
    template_name = "dashboard/update_asset.html"
    success_url = reverse_lazy('dashboard:view_asset')

@method_decorator(login_required, name='dispatch')
class CreateCategoryView(generic.CreateView):
    form_class = CategoryForm
    model = Category
    template_name = "dashboard/create_category.html"
    success_url = reverse_lazy('dashboard:view_category')


@method_decorator(login_required, name='dispatch')
class CategoryView(generic.ListView):
    template_name="dashboard/category_list.html"
    def get_queryset(self):
        return Category.objects.all()

@method_decorator(login_required, name='dispatch')
class CategoryDeleteView(generic.DeleteView):
    model = Category
    # Template_name = 'dashboard/category_confirm_delete.html'
    success_url = reverse_lazy('dashboard:view_category')
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

@method_decorator(login_required, name='dispatch')
class UpdateCategoryView(generic.UpdateView):
    form_class = CategoryForm
    model = Category
    template_name = "dashboard/update_category.html"
    success_url = reverse_lazy('dashboard:view_category')


class AssignAssetView(View):
    def get(self, request, *args, **kwargs):
        form = AssignAssetForm()
        return render(request,'dashboard/assign_asset.html',{'form':form})

    def post(self, request, *args, **kwargs):
        form = AssignAssetForm(request.POST or None)
        if form.is_valid():
            email= form.cleaned_data['employee']
            asset= form.cleaned_data['asset']
            expire= form.cleaned_data['expire_on']
            object=form.save(commit=False)
            employee=Employee.objects.get(email=email)
            name=employee.name
            print(name)
            object.release=True
            object.save()
            subject = 'welcome to GFG world'
            message = f'Hi {name}, You have got {asset}. for {expire}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, ]
            send_mail( subject, message, email_from, recipient_list )

        return HttpResponseRedirect("/view_assign_asset")
    
class ReleaseAssetView(View):
    def get(self,request,id):
        queryset=AssignAsset.objects.filter(id=id).update(release=False)
        return HttpResponseRedirect("/view_assign_asset")

class AssignAssetListView(generic.ListView):
    model = AssignAsset
    template_name = "dashboard/assign_asset_list.html"
    queryset = AssignAsset.objects.filter(release=True)