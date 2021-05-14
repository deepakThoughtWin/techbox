from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'email' : forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}),
       }
        fields=['username','email']
LANGUAGE_CHOICES =(
    ("hi", "Hindi"),
    ("en-us", "English"),
)
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        widgets = {
            'language_code' : forms.Select(choices=LANGUAGE_CHOICES,attrs={'class':'form-control'}),
            'contact_number' : forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'age' : forms.TextInput(attrs={'class':'form-control','placeholder':'Age'}),
            'city' : forms.TextInput(attrs={'class':'form-control','placeholder':'City'}),
            'about' : forms.TextInput(attrs={'class':'form-control','placeholder':'About'}),
            'gender' : forms.TextInput(attrs={'class':'form-control','placeholder':'Gender'}),
            'profile_pic' : forms.FileInput(attrs={'class':'form-control'}),
            'occupation' : forms.TextInput(attrs={'class':'form-control','placeholder':'Occupation'}),
       }
        fields='__all__'
        exclude = ('user','upgraded','upgraded_on',)