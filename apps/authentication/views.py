from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views import View
from .forms import UserUpdateForm,ProfileUpdateForm
from django.contrib import messages

 
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
        if request.user.is_authenticated:
                return redirect('home')
        else:
            form = UserCreationForm()
            return render(request, 'registration/register.html', {'form': form})



class ProfileView(View):
    def post(self, request):
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        u_form = UserUpdateForm(request.POST,instance=request.user)
        if p_form.is_valid() and u_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,'Your Profile has been updated!')
            return redirect('profile')
    def get(self,request):
        p_form = ProfileUpdateForm(instance=request.user.profile)
        u_form = UserUpdateForm(instance=request.user)
        context={'p_form': p_form, 'u_form': u_form}
        return render(request, 'users/profile.html',context )