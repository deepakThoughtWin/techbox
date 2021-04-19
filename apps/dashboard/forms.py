from django.forms.models import ModelChoiceField
from apps.dashboard.models import Asset, Category, Designation, Employee
from django import forms
# from searchableselect.widgets import SearchableSelect


class EmployeeForm(forms.ModelForm):  
    class Meta:
        model = Employee
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'email' : forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}),
            'designation': forms.Select(attrs={'class':'form-control'}),
            'phone' : forms.TextInput(attrs={'minlength': 10, 'maxlength': 15, 'required': True, 'type': 'number','class':'form-control'}), 
            'address' : forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}),
       }
        fields = "__all__"
        exclude =('status',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['designation'].queryset = Designation.objects.all()
    
    # def clean_email(self):
    #       email = self.cleaned_data['email']
    #       print(email)
    #       if Employee.objects.filter(email=email).exists():
    #           raise forms.ValidationError("Already Exists")
    #       return email
        
class DesignationForm(forms.ModelForm):  
    
    class Meta:
        model = Designation
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Designation'}),  
        }
        fields = "__all__"
        

    
    
class AssetForm(forms.ModelForm):  
    class Meta:
        model = Asset
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'category' : forms.Select(attrs={'class':'form-control'}),
            'model_number': forms.TextInput(attrs={'class':'form-control','placeholder':'Model Number'}),
            'availability' : forms.TextInput(attrs={'minlength': 10, 'maxlength': 15, 'required': True, 'type': 'number','class':'form-control'}), 
            'employee' : forms.Select(attrs={'class':'form-control'}),
            'expire_date' : forms.TextInput(attrs={'class':'form-control','type': 'date'}),
       }
        fields = "__all__"
        exclude =('availability',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all()
        self.fields['employee'].queryset = Employee.objects.all()