from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views import View
 
# Views
class Registration(View):
    def post(self,request):
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                user = authenticate(username = username, password = password)
                login(request, user)
                return redirect('home')
    def get(self,request):
        form = UserCreationForm()
        return render(request, 'registration/register.html', {'form': form})