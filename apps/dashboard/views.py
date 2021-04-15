from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class IndexView(generic.TemplateView):
    template_name ="dashboard/index.html"

