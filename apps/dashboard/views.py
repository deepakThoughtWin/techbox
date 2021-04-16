from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from .forms import EmployeeForm
from .models import Employee

@method_decorator(login_required, name='dispatch')
class IndexView(generic.TemplateView):
    template_name ="dashboard/index.html"

class CreateEmployeeView(SuccessMessageMixin,generic.CreateView):
    form_class = EmployeeForm
    model = Employee
    template_name = "dashboard/create_employee.html"
    success_url ="/employee/"
    success_message = "Employee was Created successfully"
    # def form_valid(self, form):
    #     obj = form.save(commit=False)
    #     obj.author = self.request.user
    #     return super(CreatePostView, self).form_valid(form)

class EmployeeView(generic.ListView):
    template_name="dashboard/employee_list.html"
    def get_queryset(self):
        return Employee.objects.all()