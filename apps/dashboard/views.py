from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from apps.dashboard.forms import AssetForm, EmployeeForm,DesignationForm
from apps.dashboard.models import Asset, Designation, Employee
from django.urls import reverse_lazy


@method_decorator(login_required, name='dispatch')
class IndexView(generic.TemplateView):
    template_name ="dashboard/index.html"

@method_decorator(login_required, name='dispatch')
class CreateEmployeeView(SuccessMessageMixin,generic.CreateView):
    form_class = EmployeeForm
    model = Employee
    template_name = "dashboard/create_employee.html"
    success_url ="/view_employee/"
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
    Template_name = 'dshboard/employee_confirm_delete.html'
    success_url = reverse_lazy('dashboard:view_employee')

@method_decorator(login_required, name='dispatch')
class UpdateEmployeeView(generic.UpdateView):
    form_class = EmployeeForm
    model = Employee
    template_name = "dashboard/update_employee.html"
    success_url ="/view_employee/"
    
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
    success_url ="/view_designation/"
    success_message = "Employee was Created successfully"

@method_decorator(login_required, name='dispatch')
class DesignationDeleteView(generic.DeleteView):
    model = Designation
    Template_name = 'dashboard/designaion_confirm_delete.html'
    success_url = reverse_lazy('dashboard:view_designation')

@method_decorator(login_required, name='dispatch')
class UpdateDesignationView(generic.UpdateView):
    form_class = DesignationForm
    model = Designation
    template_name = "dashboard/update_designation.html"
    success_url ="/view_designation/"


class CreateAssetView(SuccessMessageMixin,generic.CreateView):
    form_class = AssetForm
    model = Asset
    template_name = "dashboard/create_asset.html"
    success_url ="/asset/"
